import torch
import torch.nn as nn
import torch.nn.functional as F

class Bottleneck(nn.Module):
    def __init__(self, in_channels, out_channels, expansion_factor, stride):
        super(Bottleneck, self).__init__()
        mid_channels = in_channels * expansion_factor
        self.stride = stride
        self.use_res_connect = self.stride == 1 and in_channels == out_channels

        self.conv = nn.Sequential(
            # 1x1 pointwise convolution (expand)
            nn.Conv2d(in_channels, mid_channels, kernel_size=1, bias=False),
            nn.BatchNorm2d(mid_channels),
            nn.ReLU6(inplace=True),
            # 3x3 depthwise convolution
            nn.Conv2d(mid_channels, mid_channels, kernel_size=3, stride=stride, padding=1, groups=mid_channels, bias=False),
            nn.BatchNorm2d(mid_channels),
            nn.ReLU6(inplace=True),
            # 1x1 pointwise convolution (compress)
            nn.Conv2d(mid_channels, out_channels, kernel_size=1, bias=False),
            nn.BatchNorm2d(out_channels),
        )

    def forward(self, x):
        if self.use_res_connect:
            return x + self.conv(x)
        else:
            return self.conv(x)


class MobileFaceNet(nn.Module):
    def __init__(self, embedding_size=128):
        super(MobileFaceNet, self).__init__()

        # Initial layers
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=2, padding=1, bias=False)  # conv3x3
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU6(inplace=True)
        
        # Sequence of bottlenecks based on the architecture table
        self.bottlenecks = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=3, groups=64, padding=1, stride=1, bias=False),  # Depthwise conv
            nn.BatchNorm2d(64),
            Bottleneck(64, 64, expansion_factor=2, stride=2),  # Bottleneck 1
            Bottleneck(64, 64, expansion_factor=2, stride=1),  # Bottleneck repeat n=5
            Bottleneck(64, 128, expansion_factor=4, stride=2),  # Bottleneck 2
            Bottleneck(128, 128, expansion_factor=2, stride=1),  # Bottleneck repeat n=6
            Bottleneck(128, 128, expansion_factor=4, stride=2),  # Bottleneck 3
            Bottleneck(128, 128, expansion_factor=2, stride=1),  # Bottleneck repeat n=2
        )
        
        # 1x1 convolution and Global Depthwise Convolution
        self.conv2 = nn.Conv2d(128, 512, kernel_size=1, bias=False)  # conv1x1
        self.bn2 = nn.BatchNorm2d(512)
        self.gdconv = nn.Conv2d(512, 512, kernel_size=7, groups=512, bias=False)  # GDConv7x7
        self.bn3 = nn.BatchNorm2d(512)

        # Linear layers for feature embedding
        self.conv3 = nn.Conv2d(512, embedding_size, kernel_size=1, bias=False)  # conv1x1
        self.bn4 = nn.BatchNorm2d(embedding_size)
        
        self.flatten = nn.Flatten()

    def forward(self, x):
        # Initial conv layer
        x = self.relu(self.bn1(self.conv1(x)))
        
        # Bottlenecks
        x = self.bottlenecks(x)

        # 1x1 conv followed by global depthwise conv
        x = self.relu(self.bn2(self.conv2(x)))
        x = self.relu(self.bn3(self.gdconv(x)))

        # Final embedding layer
        x = self.conv3(x)
        x = self.bn4(x)

        # Flatten to produce the final embedding
        x = self.flatten(x)
        return x

# Example usage:
model = MobileFaceNet(embedding_size=128)
input_tensor = torch.randn(1, 3, 112, 112)  # Example input
output = model(input_tensor)
print(output.shape)  # Should return (1, 128), i.e., 128-dimensional face embedding
