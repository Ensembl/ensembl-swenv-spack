# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlAlienBuildPluginDownloadGitlab(PerlPackage):
    """Alien::Build plugin to download from GitLab"""

    homepage = "https://metacpan.org/pod/Alien::Build::Plugin::Download::GitLab"
    url = "https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Build-Plugin-Download-GitLab-0.01.tar.gz"

    maintainers("EbiArnie")

    version("0.01", sha256="c1f089c8ea152a789909d48a83dbfcf2626f773daf30431c8622582b26aba902")

    depends_on("perl@5.8.4:", type=("build", "link", "run", "test"))
    depends_on("perl-alien-build", type=("run"))
    depends_on("perl-path-tiny", type=("run"))
    depends_on("perl-test2-suite", type=("test"))
    depends_on("perl-uri", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
