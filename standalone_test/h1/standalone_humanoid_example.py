# Copyright (c) 2020-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": False}) # we can also run as headless.

import carb
import numpy as np
import omni
import omni.appwindow  # Contains handle to keyboard
# from omni.isaac.examples.base_sample import BaseSample
# from omni.isaac.examples.humanoid.h1 import H1FlatTerrainPolicy

from omni.isaac.core.utils.nucleus import get_assets_root_path
from omni.isaac.core.utils.stage import add_reference_to_stage
from omni.isaac.core.robots import Robot

from omni.isaac.core import World
from h1 import H1FlatTerrainPolicy


world = World()
# await world.initialize_simulation_context_async()
world.scene.add_default_ground_plane(
    z_position=0,
    name="default_ground_plane",
    prim_path="/World/defaultGroundPlane",
    static_friction=0.2,
    dynamic_friction=0.2,
    restitution=0.01,
)


# assets_root_path = get_assets_root_path()
# if assets_root_path is None:
#     carb.log_error("Could not find nucleus server with /Isaac folder")
# asset_path = assets_root_path + "/Isaac/Robots/Jetbot/jetbot.usd"
# # breakpoint()
# add_reference_to_stage(usd_path=asset_path, prim_path="/World/Fancy_Robot123")
# jetbot_robot = world.scene.add(Robot(prim_path="/World/Fancy_Robot123", name="fancy_robot123"))

# h1 = H1FlatTerrainPolicy(
#     prim_path="/World/H1",
#     name="H1",
#     position=np.array([0, 0, 1.05]),
# )

world.reset()
for i in range(500):
    print(i)
    world.step(render=True) # execute one physics step and one rendering step

simulation_app.close() # close Isaac Sim

breakpoint()

