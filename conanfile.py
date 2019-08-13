from conans import ConanFile, CMake, tools


class LibbarConan(ConanFile):
    name = "libbar"
    version = "0.2"
    license = "<Put the package license here>"
    author = "Carsten Haubold <carstenhaubold@googlemail.com>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Libbar here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "libbar/*"

    def build(self):
        cmake = CMake(self, generator="Unix Makefiles")
        cmake.configure(source_folder="libbar")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include/libbar", src="libbar/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["libbar"]

