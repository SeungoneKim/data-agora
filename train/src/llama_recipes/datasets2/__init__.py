# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from functools import partial

from llama_recipes.datasets2.grammar_dataset.grammar_dataset import get_dataset as get_grammar_dataset
from llama_recipes.datasets2.alpaca_dataset import InstructionDataset as get_alpaca_dataset
from llama_recipes.datasets2.custom_dataset import get_custom_dataset
from llama_recipes.datasets2.samsum_dataset import get_preprocessed_samsum as get_samsum_dataset
from llama_recipes.datasets2.toxicchat_dataset import get_llamaguard_toxicchat_dataset as get_llamaguard_toxicchat_dataset
from llama_recipes.datasets2.synthetic_dataset import SyntheticDataset as get_synthetic_dataset

DATASET_PREPROC = {
    "alpaca_dataset": partial(get_alpaca_dataset),
    "grammar_dataset": get_grammar_dataset,
    "samsum_dataset": get_samsum_dataset,
    "custom_dataset": get_custom_dataset,
    "llamaguard_toxicchat_dataset": get_llamaguard_toxicchat_dataset,
    "math_gpt4o_mini_25000": partial(get_synthetic_dataset),
    "math_gpt4o_mini_50000": partial(get_synthetic_dataset),
    "code_gpt4o_mini_10000": partial(get_synthetic_dataset),
    "code_gpt4o_mini_25000": partial(get_synthetic_dataset),
    "code_gpt4o_mini_50000": partial(get_synthetic_dataset),
    "general_gpt4o_mini_10000": partial(get_synthetic_dataset),
    "general_gpt4o_mini_25000": partial(get_synthetic_dataset),
    "general_gpt4o_mini_50000": partial(get_synthetic_dataset),
    "math_gpt4o_25000": partial(get_synthetic_dataset),
    "code_gpt4o_10000": partial(get_synthetic_dataset),
    "general_gpt4o_10000": partial(get_synthetic_dataset),
    "math_llama3_70b_25000": partial(get_synthetic_dataset),
    "math_llama3_70b_50000": partial(get_synthetic_dataset),
    "general_llama3_70b_10000": partial(get_synthetic_dataset),
    "general_llama3_70b_25000": partial(get_synthetic_dataset),
    "general_llama3_70b_50000": partial(get_synthetic_dataset),
    "code_llama3_70b_10000": partial(get_synthetic_dataset),
    "code_llama3_70b_25000": partial(get_synthetic_dataset),
    "code_llama3_70b_50000": partial(get_synthetic_dataset),
    "math_llama3_405b_25000": partial(get_synthetic_dataset),
    "code_llama3_405b_10000": partial(get_synthetic_dataset),
    "general_llama3_405b_10000": partial(get_synthetic_dataset),
    "math_llama3_8b_25000": partial(get_synthetic_dataset),
    "math_llama3_8b_50000": partial(get_synthetic_dataset),
    "general_llama3_8b_10000": partial(get_synthetic_dataset),
    "general_llama3_8b_25000": partial(get_synthetic_dataset),
    "general_llama3_8b_50000": partial(get_synthetic_dataset),
    "code_llama3_8b_10000": partial(get_synthetic_dataset),
    "code_llama3_8b_25000": partial(get_synthetic_dataset),
    "code_llama3_8b_50000": partial(get_synthetic_dataset),
    "math_claude3_sonnet_25000": partial(get_synthetic_dataset),
    "code_claude3_sonnet_10000": partial(get_synthetic_dataset),
    "general_claude3_sonnet_10000": partial(get_synthetic_dataset),
    "general_seed_data": partial(get_synthetic_dataset),
    "code_seed_data": partial(get_synthetic_dataset),
    "math_seed_data": partial(get_synthetic_dataset),
    "magpie_math_gpt4o_mini_10000": partial(get_synthetic_dataset),
    "magpie_math_gpt4o_mini_25000": partial(get_synthetic_dataset),
    "magpie_math_gpt4o_mini_50000": partial(get_synthetic_dataset),
    "magpie_code_gpt4o_mini_10000": partial(get_synthetic_dataset),
    "magpie_code_gpt4o_mini_25000": partial(get_synthetic_dataset),
    "magpie_code_gpt4o_mini_50000": partial(get_synthetic_dataset),
    "magpie_general_gpt4o_mini_10000": partial(get_synthetic_dataset),
    "magpie_general_gpt4o_mini_25000": partial(get_synthetic_dataset),
    "magpie_general_gpt4o_mini_50000": partial(get_synthetic_dataset),
    "magpie_math_gpt4o_10000": partial(get_synthetic_dataset),
    "magpie_code_gpt4o_10000": partial(get_synthetic_dataset),
    "magpie_general_gpt4o_10000": partial(get_synthetic_dataset),
    "magpie_math_llama3_70b_10000": partial(get_synthetic_dataset),
    "magpie_math_llama3_70b_25000": partial(get_synthetic_dataset),
    "magpie_math_llama3_70b_50000": partial(get_synthetic_dataset),
    "magpie_general_llama3_70b_10000": partial(get_synthetic_dataset),
    "magpie_general_llama3_70b_25000": partial(get_synthetic_dataset),
    "magpie_general_llama3_70b_50000": partial(get_synthetic_dataset),
    "magpie_code_llama3_70b_10000": partial(get_synthetic_dataset),
    "magpie_code_llama3_70b_25000": partial(get_synthetic_dataset),
    "magpie_code_llama3_70b_50000": partial(get_synthetic_dataset),
    "magpie_math_llama3_405b_10000": partial(get_synthetic_dataset),
    "magpie_code_llama3_405b_10000": partial(get_synthetic_dataset),
    "magpie_general_llama3_405b_10000": partial(get_synthetic_dataset),
    "magpie_math_llama3_8b_10000": partial(get_synthetic_dataset),
    "magpie_math_llama3_8b_25000": partial(get_synthetic_dataset),
    "magpie_math_llama3_8b_50000": partial(get_synthetic_dataset),
    "magpie_general_llama3_8b_10000": partial(get_synthetic_dataset),
    "magpie_general_llama3_8b_25000": partial(get_synthetic_dataset),
    "magpie_general_llama3_8b_50000": partial(get_synthetic_dataset),
    "magpie_code_llama3_8b_10000": partial(get_synthetic_dataset),
    "magpie_code_llama3_8b_25000": partial(get_synthetic_dataset),
    "magpie_code_llama3_8b_50000": partial(get_synthetic_dataset),
    "magpie_math_claude3_sonnet_10000": partial(get_synthetic_dataset),
    "magpie_code_claude3_sonnet_10000": partial(get_synthetic_dataset),
    "magpie_general_claude3_sonnet_10000": partial(get_synthetic_dataset),
    "webinstruct_math_gpt4o_mini_10000": partial(get_synthetic_dataset),
    "webinstruct_math_gpt4o_mini_25000": partial(get_synthetic_dataset),
    "webinstruct_math_gpt4o_mini_50000": partial(get_synthetic_dataset),
    "webinstruct_general_gpt4o_mini_10000": partial(get_synthetic_dataset),
    "webinstruct_general_gpt4o_mini_25000": partial(get_synthetic_dataset),
    "webinstruct_general_gpt4o_mini_50000": partial(get_synthetic_dataset),
    "webinstruct_code_gpt4o_mini_10000": partial(get_synthetic_dataset),
    "webinstruct_code_gpt4o_mini_25000": partial(get_synthetic_dataset),
    "webinstruct_code_gpt4o_mini_50000": partial(get_synthetic_dataset),
    "webinstruct_math_gpt4o_10000": partial(get_synthetic_dataset),
    "webinstruct_general_gpt4o_10000": partial(get_synthetic_dataset),
    "webinstruct_code_gpt4o_10000": partial(get_synthetic_dataset),
    "webinstruct_math_llama3_70b_10000": partial(get_synthetic_dataset),
    "webinstruct_math_llama3_70b_25000": partial(get_synthetic_dataset),
    "webinstruct_math_llama3_70b_50000": partial(get_synthetic_dataset),
    "webinstruct_general_llama3_70b_10000": partial(get_synthetic_dataset),
    "webinstruct_general_llama3_70b_25000": partial(get_synthetic_dataset),
    "webinstruct_general_llama3_70b_50000": partial(get_synthetic_dataset),
    "webinstruct_code_llama3_70b_10000": partial(get_synthetic_dataset),
    "webinstruct_code_llama3_70b_25000": partial(get_synthetic_dataset),
    "webinstruct_code_llama3_70b_50000": partial(get_synthetic_dataset),
    "webinstruct_math_llama3_405b_10000": partial(get_synthetic_dataset),
    "webinstruct_general_llama3_405b_10000": partial(get_synthetic_dataset),
    "webinstruct_code_llama3_405b_10000": partial(get_synthetic_dataset),
    "webinstruct_math_llama3_8b_10000": partial(get_synthetic_dataset),
    "webinstruct_math_llama3_8b_25000": partial(get_synthetic_dataset),
    "webinstruct_math_llama3_8b_50000": partial(get_synthetic_dataset),
    "webinstruct_general_llama3_8b_25000": partial(get_synthetic_dataset),
    "webinstruct_general_llama3_8b_50000": partial(get_synthetic_dataset),
    "webinstruct_code_llama3_8b_10000": partial(get_synthetic_dataset),
    "webinstruct_code_llama3_8b_25000": partial(get_synthetic_dataset),
    "webinstruct_code_llama3_8b_50000": partial(get_synthetic_dataset),
    "webinstruct_math_claude3_sonnet_10000": partial(get_synthetic_dataset),
    "webinstruct_general_claude3_sonnet_10000": partial(get_synthetic_dataset),
    "webinstruct_code_claude3_sonnet_10000": partial(get_synthetic_dataset),
    "fineweb_edu_general_gpt4o_mini_10000": partial(get_synthetic_dataset),
    "fineweb_edu_general_gpt4o_mini_25000": partial(get_synthetic_dataset),
    "fineweb_edu_general_gpt4o_mini_50000": partial(get_synthetic_dataset),
    "fineweb_edu_general_gpt4o_10000": partial(get_synthetic_dataset),
    "fineweb_edu_general_llama3_70b_10000": partial(get_synthetic_dataset),
    "fineweb_edu_general_llama3_70b_25000": partial(get_synthetic_dataset),
    "fineweb_edu_general_llama3_70b_50000": partial(get_synthetic_dataset),
    "fineweb_edu_general_llama3_405b_10000": partial(get_synthetic_dataset),
    "fineweb_edu_general_llama3_8b_10000": partial(get_synthetic_dataset),
    "fineweb_edu_general_llama3_8b_25000": partial(get_synthetic_dataset),
    "fineweb_edu_general_llama3_8b_50000": partial(get_synthetic_dataset),
    "fineweb_edu_general_claude3_sonnet_10000": partial(get_synthetic_dataset),
    "ablation1_math_llama3_8b_instruct": partial(get_synthetic_dataset),
    "ablation1_general_llama3_8b_instruct": partial(get_synthetic_dataset),
    "ablation1_code_llama3_8b_instruct": partial(get_synthetic_dataset),
    "ablation2_math_llama3_8b_instruct": partial(get_synthetic_dataset),
    "ablation2_general_llama3_8b_instruct": partial(get_synthetic_dataset),
    "ablation2_code_llama3_8b_instruct": partial(get_synthetic_dataset),
    "ablation3_math_llama3_8b_instruct": partial(get_synthetic_dataset),
    "ablation3_general_llama3_8b_instruct": partial(get_synthetic_dataset),
    "ablation3_code_llama3_8b_instruct": partial(get_synthetic_dataset),
    "ablation1_math_llama3_70b_instruct": partial(get_synthetic_dataset),
    "ablation1_general_llama3_70b_instruct": partial(get_synthetic_dataset),
    "ablation1_code_llama3_70b_instruct": partial(get_synthetic_dataset),
    "ablation2_math_llama3_70b_instruct": partial(get_synthetic_dataset),
    "ablation2_general_llama3_70b_instruct": partial(get_synthetic_dataset),
    "ablation2_code_llama3_70b_instruct": partial(get_synthetic_dataset),
    "ablation3_math_llama3_70b_instruct": partial(get_synthetic_dataset),
    "ablation3_general_llama3_70b_instruct": partial(get_synthetic_dataset),
    "ablation3_code_llama3_70b_instruct": partial(get_synthetic_dataset),
    "ablation1_math_gpt4o_mini": partial(get_synthetic_dataset),
    "ablation1_general_gpt4o_mini": partial(get_synthetic_dataset),
    "ablation1_code_gpt4o_mini": partial(get_synthetic_dataset),
    "ablation2_math_gpt4o_mini": partial(get_synthetic_dataset),
    "ablation2_general_gpt4o_mini": partial(get_synthetic_dataset),
    "ablation2_code_gpt4o_mini": partial(get_synthetic_dataset),
    "ablation3_math_gpt4o_mini": partial(get_synthetic_dataset),
    "ablation3_general_gpt4o_mini": partial(get_synthetic_dataset),
    "ablation3_code_gpt4o_mini": partial(get_synthetic_dataset),
}