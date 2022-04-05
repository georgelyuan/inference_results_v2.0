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

import os
import sys
sys.path.insert(0, os.getcwd())

from code.common.constants import Benchmark, Scenario
from code.common.systems.system_list import KnownSystem
from configs.configuration import *
from configs.rnnt import GPUBaseConfig


class SingleStreamGPUBaseConfig(GPUBaseConfig):
    scenario = Scenario.SingleStream
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    audio_batch_size = 1
    audio_fp16_input = True
    dali_batches_issue_ahead = 1
    dali_pipeline_depth = 1
    use_graphs = True
    disable_encoder_plugin = True
    nobatch_sorting = True
    num_warmups = 32


# SYS-220HE-FTNR_2_A2_TRT
@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A2x2(SingleStreamGPUBaseConfig):
    system = KnownSystem.A2x2
    audio_buffer_num_lines = 1
    single_stream_expected_latency_ns = 105000000
    nouse_copy_kernel = True


# SYS-220HE-FTNR_1_A2_TRT
@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A2x1(SingleStreamGPUBaseConfig):
    system = KnownSystem.A2x1
    audio_buffer_num_lines = 1
    single_stream_expected_latency_ns = 105000000
    nouse_copy_kernel = True

