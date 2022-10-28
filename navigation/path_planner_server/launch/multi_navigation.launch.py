import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import launch


def generate_launch_description():
    localization_share_dir = get_package_share_directory('localization_server')

    multi_localization_launch = launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                    localization_share_dir + '/launch/multi_localization.launch.py'))


    pathplanner_share_dir = get_package_share_directory('path_planner_server')

    multi_pathplanner_launch = launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                    pathplanner_share_dir + '/launch/multi_pathplanner.launch.py'))



    return LaunchDescription([
    Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', [os.path.join(pathplanner_share_dir, 'config', 'multi_path_planner.rviz')]]
    ),


        multi_localization_launch,

        multi_pathplanner_launch

        # MULTI Localization



        #MULTI Path planning

        #RVIZ with mutli path plannign config



    ])
