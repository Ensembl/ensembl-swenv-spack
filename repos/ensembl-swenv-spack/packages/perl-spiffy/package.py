# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlSpiffy(PerlPackage):
    """Spiffy Perl Interface Framework For You"""

    homepage = "https://metacpan.org/pod/Spiffy"
    url = "https://cpan.metacpan.org/authors/id/I/IN/INGY/Spiffy-0.46.tar.gz"

    maintainers("EbiArnie")

    version("0.46", sha256="8f58620a8420255c49b6c43c5ff5802bd25e4f09240c51e5bf2b022833d41da3")

    depends_on("perl@5.8.1:", type=("build", "link", "run", "test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
