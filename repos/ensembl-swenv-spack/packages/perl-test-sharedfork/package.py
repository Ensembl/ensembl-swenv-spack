# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestSharedfork(PerlPackage):
    """Fork test"""

    homepage = "https://metacpan.org/pod/Test::SharedFork"
    url = "https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-SharedFork-0.35.tar.gz"

    maintainers("EbiArnie")

    version("0.35", sha256="2932e865610e80758f764c586757ef8e11db1284d958e25e4b7a85098414c59f")

    depends_on("perl@5.8.1:", type=("build", "link", "run", "test"))
    depends_on("perl-test-requires", type=("test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
