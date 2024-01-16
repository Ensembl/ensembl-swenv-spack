# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Mmseqs2(CMakePackage):
    """MMseqs2 (Many-against-Many sequence searching) is a software suite to
    search and cluster huge protein and nucleotide sequence sets"""

    homepage = "https://github.com/soedinglab/MMseqs2"
    url = "https://github.com/soedinglab/MMseqs2/archive/refs/tags/14-7e284.tar.gz"
    git = "https://github.com/soedinglab/MMseqs2.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("14-7e284", sha256="a15fd59b121073fdcc8b259fc703e5ce4c671d2c56eb5c027749f4bd4c28dfe1")
    version("13-45111", sha256="6444bb682ebf5ced54b2eda7a301fa3e933c2a28b7661f96ef5bdab1d53695a2")

    def url_for_version(self, version):
        url_fmt = "https://github.com/soedinglab/MMseqs2/archive/refs/tags/{0}-{1}.tar.gz"
        return url_fmt.format(version[0], version[1])

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    depends_on("bash", type="build")
    depends_on("bzip2")
    depends_on("gawk", type="build")
    depends_on("git", type="build")
    depends_on("grep", type="build")
    depends_on("tar", type="build")
    depends_on("wget")
    depends_on("xxd-standalone", type="build")
    depends_on("zlib")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
