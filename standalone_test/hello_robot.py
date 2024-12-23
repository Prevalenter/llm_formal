from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": False}) # we can also run as headless.

# from omni.isaac.examples.base_sample import BaseSample
from omni.isaac.core.utils.types import ArticulationAction
from omni.isaac.core.utils.nucleus import get_assets_root_path
from omni.isaac.core.utils.stage import add_reference_to_stage
from omni.isaac.core.robots import Robot
import numpy as np
import carb

from omni.isaac.core import World
world = World()
world.scene.add_default_ground_plane()

assets_root_path = get_assets_root_path()
if assets_root_path is None:
    carb.log_error("Could not find nucleus server with /Isaac folder")
asset_path = assets_root_path + "/Isaac/Robots/Jetbot/jetbot.usd"
# breakpoint()
add_reference_to_stage(usd_path=asset_path, prim_path="/World/Fancy_Robot123")
jetbot_robot = world.scene.add(Robot(prim_path="/World/Fancy_Robot123", name="fancy_robot123"))

world.reset()

for i in range(500):
    # position, orientation = fancy_cube.get_world_pose()
    # linear_velocity = fancy_cube.get_linear_velocity()
    # # will be shown on terminal
    # print("Cube position is : " + str(position))
    # print("Cube's orientation is : " + str(orientation))
    # print("Cube's linear velocity is : " + str(linear_velocity))
    # we have control over stepping physics and rendering in this workflow
    # things run in sync
    jetbot_articulation_controller = jetbot_robot.get_articulation_controller()
    world.step(render=True) # execute one physics step and one rendering step
    
    jetbot_articulation_controller.apply_action(ArticulationAction(joint_positions=None,
                                                                            joint_efforts=None,
                                                                            joint_velocities=5 * np.random.rand(2,)))

simulation_app.close() # close Isaac Sim

# class HelloWorld(BaseSample):
#     def __init__(self) -> None:
#         super().__init__()
#         return

#     def setup_scene(self):
#         world = self.get_world()
#         world.scene.add_default_ground_plane()
#         assets_root_path = get_assets_root_path()
#         if assets_root_path is None:
#             carb.log_error("Could not find nucleus server with /Isaac folder")
#         asset_path = assets_root_path + "/Isaac/Robots/Jetbot/jetbot.usd"
#         add_reference_to_stage(usd_path=asset_path, prim_path="/World/Fancy_Robot")
#         jetbot_robot = world.scene.add(Robot(prim_path="/World/Fancy_Robot", name="fancy_robot"))
#         return

#     async def setup_post_load(self):
#         self._world = self.get_world()
#         self._jetbot = self._world.scene.get_object("fancy_robot")
#         # This is an implicit PD controller of the jetbot/ articulation
#         # setting PD gains, applying actions, switching control modes..etc.
#         # can be done through this controller.
#         # Note: should be only called after the first reset happens to the world
#         self._jetbot_articulation_controller = self._jetbot.get_articulation_controller()
#         # Adding a physics callback to send the actions to apply actions with every
#         # physics step executed.
#         self._world.add_physics_callback("sending_actions", callback_fn=self.send_robot_actions)
#         return

#     def send_robot_actions(self, step_size):
#         # Every articulation controller has apply_action method
#         # which takes in ArticulationAction with joint_positions, joint_efforts and joint_velocities
#         # as optional args. It accepts numpy arrays of floats OR lists of floats and None
#         # None means that nothing is applied to this dof index in this step
#         # ALTERNATIVELY, same method is called from self._jetbot.apply_action(...)
#         self._jetbot_articulation_controller.apply_action(ArticulationAction(joint_positions=None,
#                                                                             joint_efforts=None,
#                                                                             joint_velocities=5 * np.random.rand(2,)))
#         return
    
breakpoint()
