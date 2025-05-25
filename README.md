# robotont_navigation

![ROS 2](https://img.shields.io/badge/ROS2%20-Jazzy-blue.svg) [![CI](https://github.com/robotont/robotont_navigation/actions/workflows/industrial_ci_action.yml/badge.svg)](https://github.com/robotont/robotont_navigation/actions/workflows/industrial_ci_action.yml) ![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)

## **Overview**
Navigation base for Robotont.
## **Table of Contents**
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Building the Package](#building-the-package)
- [Launch Files](#launch-files)
- [License](#license)

---

## **Installation**

### **1. Clone the Repository**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>/src
git clone https://github.com/robotont/robotont_navigation.git
```

## **Dependencies**
### **1. List of dependencies**
1.1. nav2_bt_navigator<br>
1.2. nav2_controller<br>
1.3. nav2_planner<br>
1.4. nav2_behaviors<br>
1.5. nav2_lifecycle_manager
### **2. Install dependencies**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>
rosdep install --from-paths src --ignore-src -r -y
```

## **Building the package**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>
colcon build --packages-select robotont_navigation
```

## **Launch files**
### **1. Source workspace**
```bash
source ~/<YOUR_WORKSPACE_NAME_HERE>/install/setup.bash
```
## 2. Available Launch Files

### 2.1. `nav2_bringup.launch.py`
Launches the core navigation stack nodes with configurable parameters.

**Supported Parameters**

| Name           | Description                                   | Options/Default          |
|----------------|-----------------------------------------------|--------------------------|
| `use_sim_time` | Use simulation time (Gazebo/Sim)              | `true` (default), `false`|
| `params_file`  | Path to navigation parameter YAML file         | `nav2_params.yaml` (default) |

**Example: Launch with default parameters**
```bash
ros2 launch robotont_navigation nav2_bringup.launch.py
```

**Example: Launch with custom parameters**
```bash
ros2 launch robotont_navigation nav2_bringup.launch.py params_file:=path_to_your_custom_conf_file.yaml
```

## **License**
This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for more information.
