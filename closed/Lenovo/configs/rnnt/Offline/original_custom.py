# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class A16X8(OfflineGPUBaseConfig):
    system = KnownSystem.A16x8

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    input_dtype: str = ''
    map_path: str = ''
    precision: str = ''
    tensor_path: str = ''

    # Optional fields:
    active_sms: int = 0
    audio_batch_size: int = 0
    audio_buffer_num_lines: int = 0
    audio_fp16_input: bool = False
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    dali_batches_issue_ahead: int = 0
    dali_pipeline_depth: int = 0
    disable_encoder_plugin: bool = False
    instance_group_count: int = 0
    max_queue_delay_usec: int = 0
    max_seq_length: int = 0
    model_path: str = ''
    nobatch_sorting: bool = False
    noenable_audio_processing: bool = False
    nopipelined_execution: bool = False
    nouse_copy_kernel: bool = False
    num_warmups: int = 0
    offline_expected_qps: int = 0
    performance_sample_count_override: int = 0
    preferred_batch_size: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    use_jemalloc: bool = False
    use_spin_wait: bool = False
    workspace_size: int = 0


