#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yusaku Aka
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build --packages-select dzone_filter > /dev/null
source install/setup.bash

timeout 20 bash -c "
    source /opt/ros/humble/setup.bash && 
    source install/setup.bash && 
    ros2 launch dzone_filter filter_launch.py
" > /tmp/dzone_test.log 2>&1

if grep -q "0.15" /tmp/dzone_test.log; then
	exit 0
else
	cat /tmp/dzone_test.log
	exit 1
fi
