![github_social_logo](https://github.com/falkhofmann/nuke_kombinat/assets/21419051/93ff41e8-9f68-4bb2-8753-fa8bb7723225)

# General
This repository aims to grow and develop over time.
At the time writing (02/2024) this shall give a solid foundation to setup Nuke with menus and knob defaults. As example where to hook up tools and gizmos, I placed some of each as examples into this repository.
The [wiki](https://github.com/falkhofmann/nuke_kombinat/wiki) shall be udpated also soon with each individual tool and gizmos.

# Start up
The entire start up process with menus, paths and knob defaults are placed under [kombinat_start_up](./kombinat_start_up/) to keep the toplevel of this repository clean.

# Tools
With the tools package I am aiming for python driven code. These tools are located under [kombinat_tools](./kombinat_tools). 
As current example is one of the tools i have been using longer than a decade.

# Gizmos
Gizmos are located under [kombinat_gizmos](./kombinat_gizmos). Those are the usual custom nodes you might be familiar with. There are no subfolders to avoid a long pluginPath. Rather the menu is defined via a python configuration.

# Knob Defaults
Knob defaults are stored as a .json file. In the near future I'll extend the functionality to save them out of nuke without any manual typing.

# Utilities
A separate package is dedicated for [utility functions](./kombinat_utils). These are commonly used across different tools to avoid code duplications.
One specific file are more dedicated for other developers. 
This one includes ATM context managers for:
- Measuring the time for tools during development.
- Save and restore node selections during any other script.
- Pause and unpause the viewer when running other scripts to avoid slow downs.

Further more there are utility modules for the nodegraph as well as for the viewer.

# Future
My current plan is to cmobine [other public repositories](https://github.com/falkhofmann?tab=repositories) of mine into this repository and to have a unified place to provide those as well as already integreated into menus etc.

# Feedback
Since I am always looking for feedback, please feel free to write an issue here, on what can be improved or contact me in any other way. 
