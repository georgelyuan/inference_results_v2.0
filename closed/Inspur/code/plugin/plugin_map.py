# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Dict storing the loading path of the TRT plugins built under TRT
# The path is relative to "build/plugins"
G_PLUGIN_MAP = {
    "3d-unet-kits": {
        "pixelshuffle3d": "pixelShuffle3DPlugin/libpixelshuffle3dplugin.so",
        "conv3d1x1x1k4": "conv3D1X1X1K4Plugin/libconv3D1X1X1K4Plugin.so"
    },
    "bert": None,
    "dlrm": {
        "DLRM interactions": "DLRMInteractionsPlugin/libdlrminteractionsplugin.so",
    },
    "resnet50": {
        "resnet50 opt": "Serial3Conv2dPlugin/libserial3conv2dplugin.so",
    },
    "rnnt": {
        "RNNT opt": "RNNTOptPlugin/librnntoptplugin.so",
    },
    "ssd-mobilenet": {
        "NMS opt": "NMSOptPlugin/libnmsoptplugin.so",
    },
    "ssd-resnet34": {
        "NMS opt": "NMSOptPlugin/libnmsoptplugin.so",
    },
}
