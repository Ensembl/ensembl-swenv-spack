# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestYaml(PerlPackage):
    """Testing Module for YAML Implementations"""

    homepage = "https://metacpan.org/pod/Test::YAML"
    url = "https://cpan.metacpan.org/authors/id/T/TI/TINITA/Test-YAML-1.07.tar.gz"

    maintainers("EbiArnie")

    version("1.07", sha256="1f300d034f46298cb92960912cc04bac33fb27f05b8852d8f051e110b9cd995f")

    depends_on("perl-test-base@0.89:", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
