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

from importlib import import_module
from code.common.constants import Benchmark, Scenario
from code.common.systems.system_list import KnownSystem
from configs.configuration import *

ParentConfig = import_module("configs.3d-unet")
GPUBaseConfig = ParentConfig.GPUBaseConfig
CPUBaseConfig = ParentConfig.CPUBaseConfig


class SingleStreamGPUBaseConfig(GPUBaseConfig):
    scenario = Scenario.SingleStream
    gpu_inference_streams = 1
    gpu_copy_streams = 1


class SingleStreamCPUBaseConfig(CPUBaseConfig):
    scenario = Scenario.SingleStream


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIex1(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_PCIe_40GBx1
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 780000000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIex1_HighAccuracy(A100_PCIex1):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIex1_Triton(A100_PCIex1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIex1_HighAccuracy_Triton(A100_PCIex1_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIe_80GBx1(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_PCIe_80GBx1
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 572434000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIe_80GBx1_HighAccuracy(A100_PCIe_80GBx1):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIe_80GBx1_Triton(A100_PCIe_80GBx1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIe_80GBx1_HighAccuracy_Triton(A100_PCIe_80GBx1_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class DRIVE_A100_PCIE(SingleStreamGPUBaseConfig):
    system = KnownSystem.DRIVE_A100_PCIE
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 572434000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class DRIVE_A100_PCIE_HighAccuracy(DRIVE_A100_PCIE):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class DRIVE_A100_PCIE_Triton(DRIVE_A100_PCIE):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class DRIVE_A100_PCIE_HighAccuracy_Triton(DRIVE_A100_PCIE_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIe_80GB_MIG_1x1g10gb(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_PCIe_80GB_MIG_1x1g_10gb
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 90000000000
    workspace_size = 1073741824


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIe_80GB_MIG_1x1g10gb_HighAccuracy(A100_PCIe_80GB_MIG_1x1g10gb):
    pass


@ConfigRegistry.register(HarnessType.HeteroMIG, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIe_80GB_MIG_1x1g10gb_Hetero(A100_PCIe_80GB_MIG_1x1g10gb):
    pass


@ConfigRegistry.register(HarnessType.HeteroMIG, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIe_80GB_MIG_1x1g10gb_Hetero_HighAccuracy(A100_PCIe_80GB_MIG_1x1g10gb_HighAccuracy):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIe_80GB_MIG_1x1g10gb_Triton(A100_PCIe_80GB_MIG_1x1g10gb):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIe_80GB_MIG_1x1g10gb_HighAccuracy_Triton(A100_PCIe_80GB_MIG_1x1g10gb_Triton):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIe_80GB_MIG_56x1g10gb_Triton(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_PCIe_80GB_MIG_56x1g_10gb
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 92000000000
    workspace_size = 1073741824
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIe_80GB_MIG_56x1g10gb_HighAccuracy_Triton(A100_PCIe_80GB_MIG_56x1g10gb_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIe_80GB_aarch64x1(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_PCIe_80GB_ARMx1
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 780000000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIe_80GB_aarch64x1_HighAccuracy(A100_PCIe_80GB_aarch64x1):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIe_aarch64x1(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_PCIe_40GB_ARMx1
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 780000000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIe_aarch64x1_Triton(A100_PCIe_aarch64x1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIe_aarch64x1_HighAccuracy(A100_PCIe_aarch64x1):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_PCIe_aarch64x1_HighAccuracy_Triton(A100_PCIe_aarch64x1_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_1x1g10gb(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_SXM_80GB_MIG_1x1g_10gb
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 5256000000
    start_from_device = True
    end_on_device = True
    workspace_size = 1073741824


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_1x1g10gb_HighAccuracy(A100_SXM_80GB_MIG_1x1g10gb):
    pass


@ConfigRegistry.register(HarnessType.HeteroMIG, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_1x1g10gb_Hetero(A100_SXM_80GB_MIG_1x1g10gb):
    pass


@ConfigRegistry.register(HarnessType.HeteroMIG, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_1x1g10gb_Hetero_HighAccuracy(A100_SXM_80GB_MIG_1x1g10gb_HighAccuracy):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_1x1g10gb_Triton(A100_SXM_80GB_MIG_1x1g10gb):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_1x1g10gb_HighAccuracy_Triton(A100_SXM_80GB_MIG_1x1g10gb_Triton):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_56x1g10gb_Triton(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_SXM_80GB_MIG_56x1g_10gb
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 5256000000
    start_from_device = True
    end_on_device = True
    workspace_size = 1073741824
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_56x1g10gb_HighAccuracy_Triton(A100_SXM_80GB_MIG_56x1g10gb_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GBx1(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_SXM_80GBx1
    gpu_batch_size = 1
    start_from_device = True
    end_on_device = True
    single_stream_expected_latency_ns = 552000000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GBx1_HighAccuracy(A100_SXM_80GBx1):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GBx1_Triton(A100_SXM_80GBx1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GBx1_HighAccuracy_Triton(A100_SXM_80GBx1_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_aarch64x1(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_SXM_80GB_ARMx1
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 559000000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GB_aarch64x1_HighAccuracy(A100_SXM_80GB_aarch64x1):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_aarch64x1_Triton(A100_SXM_80GB_aarch64x1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GB_aarch64x1_HighAccuracy_Triton(A100_SXM_80GB_aarch64x1_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_aarch64_MIG_1x1g10gb(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_SXM_80GB_ARM_MIG_1x1g_10gb
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 5256000000
    workspace_size = 1073741824


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GB_aarch64_MIG_1x1g10gb_HighAccuracy(A100_SXM_80GB_aarch64_MIG_1x1g10gb):
    pass


@ConfigRegistry.register(HarnessType.HeteroMIG, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_aarch64_MIG_1x1g10gb_Hetero(A100_SXM_80GB_aarch64_MIG_1x1g10gb):
    pass


@ConfigRegistry.register(HarnessType.HeteroMIG, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GB_aarch64_MIG_1x1g10gb_Hetero_HighAccuracy(A100_SXM_80GB_aarch64_MIG_1x1g10gb_HighAccuracy):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_aarch64_MIG_1x1g10gb_Triton(A100_SXM_80GB_aarch64_MIG_1x1g10gb):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM_80GB_aarch64_MIG_1x1g10gb_HighAccuracy_Triton(A100_SXM_80GB_aarch64_MIG_1x1g10gb_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM4_40GB_MIG_1x1g5gb(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_SXM4_40GB_MIG_1x1g_5gb
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 5256000000
    start_from_device = True
    end_on_device = True
    workspace_size = 1073741824


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM4_40GB_MIG_1x1g5gb_HighAccuracy(A100_SXM4_40GB_MIG_1x1g5gb):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM4_40GB_MIG_1x1g5gb_Triton(A100_SXM4_40GB_MIG_1x1g5gb):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM4_40GB_MIG_1x1g5gb_HighAccuracy_Triton(A100_SXM4_40GB_MIG_1x1g5gb_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM4_40GBx1(SingleStreamGPUBaseConfig):
    system = KnownSystem.A100_SXM4_40GBx1
    gpu_batch_size = 1
    start_from_device = True
    end_on_device = True
    single_stream_expected_latency_ns = 657000000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM4_40GBx1_HighAccuracy(A100_SXM4_40GBx1):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM4_40GBx1_Triton(A100_SXM4_40GBx1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A100_SXM4_40GBx1_HighAccuracy_Triton(A100_SXM4_40GBx1_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A2x1(SingleStreamGPUBaseConfig):
    system = KnownSystem.A2x1
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 5378800000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A2x1_Triton(A2x1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A2x1_HighAccuracy(A2x1):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A2x1_HighAccuracy_Triton(A2x1_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A2x2(SingleStreamGPUBaseConfig):
    system = KnownSystem.A2x2
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 5378800000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A2x2_HighAccuracy(A2x2):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30_MIG_1x1g6gb(SingleStreamGPUBaseConfig):
    system = KnownSystem.A30_MIG_1x1g_6gb
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 5256000000
    workspace_size = 805306368


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A30_MIG_1x1g6gb_HighAccuracy(A30_MIG_1x1g6gb):
    pass


@ConfigRegistry.register(HarnessType.HeteroMIG, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30_MIG_1x1g6gb_Hetero(A30_MIG_1x1g6gb):
    single_stream_expected_latency_ns = 5256000000


@ConfigRegistry.register(HarnessType.HeteroMIG, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A30_MIG_1x1g6gb_Hetero_HighAccuracy(A30_MIG_1x1g6gb_Hetero):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30_MIG_1x1g6gb_Triton(A30_MIG_1x1g6gb):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A30_MIG_1x1g6gb_HighAccuracy_Triton(A30_MIG_1x1g6gb_Triton):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30_MIG_32x1g6gb_Triton(SingleStreamGPUBaseConfig):
    system = KnownSystem.A30_MIG_32x1g_6gb
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 5256000000
    workspace_size = 805306368
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A30_MIG_32x1g6gb_HighAccuracy_Triton(A30_MIG_32x1g6gb_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30x1(SingleStreamGPUBaseConfig):
    system = KnownSystem.A30x1
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 1226400000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A30x1_HighAccuracy(A30x1):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30x1_Triton(A30x1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class A30x1_HighAccuracy_Triton(A30x1_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class AGX_Xavier(SingleStreamGPUBaseConfig):
    system = KnownSystem.AGX_Xavier
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 16000000000
    use_direct_host_access = True


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class AGX_Xavier_HighAccuracy(AGX_Xavier):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class AGX_Xavier_Triton(AGX_Xavier):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class AGX_Xavier_HighAccuracy_Triton(AGX_Xavier_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxQ)
class AGX_Xavier_MaxQ(AGX_Xavier):
    # power settings
    soc_gpu_freq = 1032750000
    soc_dla_freq = 115200000
    soc_cpu_freq = 1190400
    soc_emc_freq = 1331200000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxQ)
class AGX_Xavier_HighAccuracy_MaxQ(AGX_Xavier_MaxQ):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class Xavier_NX(SingleStreamGPUBaseConfig):
    system = KnownSystem.Xavier_NX
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 15450000000
    use_direct_host_access = True
    workspace_size = 1073741824


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class Xavier_NX_HighAccuracy(Xavier_NX):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class Xavier_NX_Triton(Xavier_NX):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class Xavier_NX_HighAccuracy_Triton(Xavier_NX_Triton):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxQ)
class Xavier_NX_MaxQ(Xavier_NX):
    # power settings
    soc_gpu_freq = 752250000
    soc_dla_freq = 115200000
    soc_cpu_freq = 1190400
    soc_emc_freq = 1600000000
    single_stream_expected_latency_ns = 21735000000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxQ)
class Xavier_NX_HighAccuracy_MaxQ(Xavier_NX_MaxQ):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class Orin(SingleStreamGPUBaseConfig):
    system = KnownSystem.Orin
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 2222222222
    use_direct_host_access = True


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxQ)
class Orin_MaxQ(Orin):
    soc_cpu_freq = 1036800
    soc_gpu_freq = 828750000
    soc_dla_freq = 0
    soc_emc_freq = 3199000000
    orin_num_cores = 2
    single_stream_expected_latency_ns = 32200000000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class Orin_HighAccuracy(Orin):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxQ)
class Orin_MaxQ_HighAccuracy(Orin_MaxQ):
    pass


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class T4x1(SingleStreamGPUBaseConfig):
    system = KnownSystem.T4x1
    gpu_batch_size = 1
    single_stream_expected_latency_ns = 2500000000


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class T4x1_HighAccuracy(T4x1):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class T4x1_Triton(T4x1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class T4x1_HighAccuracy_Triton(T4x1_Triton):
    pass
