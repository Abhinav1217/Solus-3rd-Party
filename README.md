# Solus-3rd-Party
Collection of 3rd Party package builder manifest for solus os.
---

Conceptually similar to [Solus 3rd-Party](https://github.com/getsolus/3rd-party/), This is my semi-personal collection of 3rd-Party Packages. 

### Why?

For long time, Solus 3rd-Party has been deprecated, and for a very valid reason. In this era of universal packages like flatpak, appimage (and snap), and improvement to container tools like docker and podman to support GUI apps, Concept of native packages might feel redundant, but I feel it still have some merrits. It doesn't have long start time like the universal solutions. A lot of companies still only provide either a .deb or .tar.gz in name of linux support. Since the `eopkg` is so awesome that it can create native package from .deb files, this felt like an optimal way to install some more apps that doesn't provide .eopkg file. 

Since no new packages will be accepted in their repo, This repo will contain collection of some newer 3rd-party packages which a lot of might want to use.

### What? 

**DO Note that this repo does not redistribute packages.**
It only provides a build manifest which can be used by the `eopkg` tools to create a native package for Solus OS. 

### Expectations !!

1. There will be no gurantee that all packages will be updated immidiatly when upstream updates. There is no automation, everything is manual.
2. New packages can be accepted, as long as process is followed and contributor is willing to accept maintaince responsibilities for submitted package. 
3. Other than generating native package (.eopkg), no attempt of modification to upstream binary will be accepted. 
4. Things can change at any time. 

### Installation.

Instructions are provided in [package-list](./package-list.md) file.
All scripts only support 64 bit x86 architecture only. 

### Contributions.

1. Open an Issue, mention all URLs and License information. Only transpiling of .tar.* and .deb is currently supported for now. 

2. Submit a PR of package you want to add. Please make sure all dependencies are mentioned. 

----

### Disclaimer

The content provided in this (“package”) is provided as a public service. You may use, copy and distribute copies of the packages in any medium, provided that you keep intact this entire notice. You may improve, modify and create derivative works of the packages or any portion of the packages, and you may copy and distribute such modifications or works. Modified works should carry a notice stating that you changed the packages and should note the date and nature of any such change. 

The packages is expressly provided “AS IS.” "WE" MAKES NO WARRANTY OF ANY KIND, EXPRESS, IMPLIED, IN FACT OR ARISING BY OPERATION OF LAW, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT AND DATA ACCURACY. "WE" NEITHER REPRESENTS NOR WARRANTS THAT THE OPERATION OF THE PACKAGES WILL BE UNINTERRUPTED OR ERROR-FREE, OR THAT ANY DEFECTS WILL BE CORRECTED. "WE" DOES NOT WARRANT OR MAKE ANY REPRESENTATIONS REGARDING THE USE OF THE PACKAGES OR THE RESULTS THEREOF, INCLUDING BUT NOT LIMITED TO THE CORRECTNESS, ACCURACY, RELIABILITY, OR USEFULNESS OF THE PACKAGES.

You are solely responsible for determining the appropriateness of using and distributing the packages and you assume all risks associated with its use, including but not limited to the risks and costs of program errors, compliance with applicable laws, damage to or loss of data, programs or equipment, and the unavailability or interruption of operation. This packages is not intended to be used in any situation where a failure could cause risk of injury or damage to property. The packages is maintained by contributors.