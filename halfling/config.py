"""Halfing configuration."""
# from dataclasses import dataclass, field


# @dataclass
# class Config:
#     """Halfing configuration object."""
#     # mandatory build info
#     project_name: str
#     compiler: str
#     sources: list
#     # output directories
#     build_dir: str = "build"
#     obj_dir: str = "obj"
#     # includes, defines, libs
#     include_paths: list = field(default_factory=list)
#     defines: list = field(default_factory=list)
#     library_paths: list = field(default_factory=list)
#     libraries: list = field(default_factory=list)
#     # compiler flags
#     common_flags: list = field(default_factory=list)
#     debug_flags: list = field(default_factory=lambda: ["-g"])
#     release_flags: list = field(default_factory=lambda: ["-O2"])

config = {}

def configure(project_name, **kwargs):
    # add required args
    config["project_name"] = project_name

    # add custom/optional args
    config.update(**kwargs)
