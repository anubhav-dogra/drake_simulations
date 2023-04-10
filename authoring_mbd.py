import numpy as np
import os
from pydrake.common import temp_directory
from pydrake.geometry import( 
                            MeshcatVisualizer, 
                            MeshcatVisualizerParams, 
                            Role, 
                            StartMeshcat)
from pydrake.math import RigidTransform, RollPitchYaw
from pydrake.multibody.parsing import Parser
from pydrake.multibody.plant import AddMultibodyPlantSceneGraph
from pydrake.systems.analysis import Simulator
from pydrake.systems.framework import DiagramBuilder
from pydrake.visualization import ModelVisualizer
meshcat = StartMeshcat()
iiwa14_model_url = ("package://home/anubhav/drake_ws/models/iiwa_description/urdf/iiwa14_rs_scanner_V1.urdf.xacro")


visualizer = ModelVisualizer(meshcat=meshcat)
visualizer.parser().AddModels(url=iiwa14_model_url)
test_mode = True if "Test_SRCDIR" in os.environ else False
visualizer.Run(loop_once=test_mode)