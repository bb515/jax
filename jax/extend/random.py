# Copyright 2023 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: import <name> as <name> is required for names to be exported.
# See PEP 484 & https://github.com/google/jax/issues/7570

from jax._src.prng import (
  # TODO(frostig,vanderplas): expose a define_prng_impl instead of the
  # PRNGImpl constructor, to leave some room for us to register or check input,
  # or to change what output type we return.
  PRNGImpl as PRNGImpl,
  seed_with_impl as seed_with_impl,
  threefry2x32_p as threefry2x32_p,
  threefry_2x32 as threefry_2x32,
  threefry_prng_impl as threefry_prng_impl,
  rbg_prng_impl as rbg_prng_impl,
  unsafe_rbg_prng_impl as unsafe_rbg_prng_impl,
)
