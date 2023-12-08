# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTest2PluginNowarnings(PerlPackage):
    """Fail if tests warn"""

    homepage = "https://metacpan.org/pod/Test2::Plugin::NoWarnings"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Test2-Plugin-NoWarnings-0.09.tar.gz"

    maintainers("EbiArnie")

    version("0.09", sha256="be3dd800042eef362bf17d2056cf9e934dee91ccce98e4f178b8fb5772f2fb74")

    depends_on("perl-ipc-run3", type=("test"))
    depends_on("perl-test2-suite", type=("test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
