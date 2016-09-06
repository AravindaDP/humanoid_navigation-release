Name:           ros-indigo-humanoid-navigation
Version:        0.4.1
Release:        1%{?dist}
Summary:        ROS humanoid_navigation package

Group:          Development/Libraries
License:        BSD,GPL 3
URL:            http://ros.org/wiki/humanoid_navigation
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-footstep-planner
Requires:       ros-indigo-gridmap-2d
Requires:       ros-indigo-humanoid-localization
BuildRequires:  ros-indigo-catkin

%description
This stack contains packages for humanoid (biped) navigation, developed at the
Humanoid Robots Lab at the Albert-Ludwigs-Universitat in Freiburg, Germany.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Sep 06 2016 Armin Hornung <HornungA@informatik.uni-freiburg.de> - 0.4.1-1
- Autogenerated by Bloom

* Mon Sep 05 2016 Armin Hornung <HornungA@informatik.uni-freiburg.de> - 0.4.1-0
- Autogenerated by Bloom

