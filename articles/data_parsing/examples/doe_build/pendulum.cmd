!
!-------------------------- Default Units for Model ---------------------------!
!
!
defaults units  &
   length = mm  &
   angle = deg  &
   force = newton  &
   mass = kg  &
   time = sec
!
defaults units  &
   coordinate_system_type = cartesian  &
   orientation_type = body313
!
!------------------------ Default Attributes for Model ------------------------!
!
!
defaults attributes  &
   inheritance = bottom_up  &
   icon_visibility = on  &
   grid_visibility = off  &
   size_of_icons = 50.0  &
   spacing_for_grid = 1000.0
!
!------------------------------ Adams/View Model ------------------------------!
!
!
model create  &
   model_name = pendulum
!
view erase
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .pendulum.steel  &
   adams_id = 1  &
   youngs_modulus = 2.07E+005  &
   poissons_ratio = 0.29  &
   density = 7.801E-006
!
!-------------------------------- Rigid Parts ---------------------------------!
!
! Create parts and their dependent markers and graphics
!
!----------------------------------- ground -----------------------------------!
!
!
! ****** Ground Part ******
!
defaults model  &
   part_name = ground
!
defaults coordinate_system  &
   default_coordinate_system = .pendulum.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .pendulum.ground.MARKER_4  &
   adams_id = 4  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .pendulum.ground  &
   material_type = .pendulum.steel
!
part attributes  &
   part_name = .pendulum.ground  &
   name_visibility = off
!
!----------------------------------- PART_2 -----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .pendulum.ground
!
part create rigid_body name_and_position  &
   part_name = .pendulum.PART_2  &
   adams_id = 2  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .pendulum.PART_2
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .pendulum.PART_2.MARKER_1  &
   adams_id = 1  &
   location = 0.0, 0.0, 0.0  &
   orientation = 320.1944289077d, 0.0d, 0.0d
!
marker create  &
   marker_name = .pendulum.PART_2.MARKER_2  &
   adams_id = 2  &
   location = 300.0, -250.0, 0.0  &
   orientation = 320.1944289077d, 0.0d, 0.0d
!
marker create  &
   marker_name = .pendulum.PART_2.cm  &
   adams_id = 5  &
   location = 150.0, -125.0, 0.0  &
   orientation = 230.1944289077d, 90.0000000082d, 90.0000000798d
!
marker create  &
   marker_name = .pendulum.PART_2.MARKER_3  &
   adams_id = 3  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .pendulum.PART_2  &
   material_type = .pendulum.steel
!
! ****** Graphics for current part ******
!
geometry create shape link  &
   link_name = .pendulum.PART_2.LINK_1  &
   i_marker = .pendulum.PART_2.MARKER_1  &
   j_marker = .pendulum.PART_2.MARKER_2  &
   width = 39.0512483795  &
   depth = 19.5256241898
!
part attributes  &
   part_name = .pendulum.PART_2  &
   color = RED  &
   name_visibility = off
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .pendulum.JOINT_1  &
   adams_id = 1  &
   i_marker_name = .pendulum.PART_2.MARKER_3  &
   j_marker_name = .pendulum.ground.MARKER_4
!
constraint attributes  &
   constraint_name = .pendulum.JOINT_1  &
   name_visibility = off
!
!----------------------------------- Forces -----------------------------------!
!
!
!----------------------------- Simulation Scripts -----------------------------!
!
!
simulation script create  &
   sim_script_name = .pendulum.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=1.0 number_of_steps=50 model_name=.model_1"
!
!---------------------------------- Accgrav -----------------------------------!
!
!
force create body gravitational  &
   gravity_field_name = gravity  &
   x_component_gravity = 0.0  &
   y_component_gravity = -9806.65  &
   z_component_gravity = 0.0
!
!----------------------------- Analysis settings ------------------------------!
!
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
geometry modify shape link  &
   link_name = .pendulum.PART_2.LINK_1  &
   width = (39.0512483795mm)  &
   depth = (19.5256241898mm)
!
material modify  &
   material_name = .pendulum.steel  &
   youngs_modulus = (2.07E+011(Newton/meter**2))  &
   density = (7801.0(kg/meter**3))
!
model display  &
   model_name = pendulum
