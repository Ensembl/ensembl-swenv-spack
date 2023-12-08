# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlListUniq(PerlPackage):
    """Extract the unique elements of a list"""

    homepage = "https://metacpan.org/pod/List::Uniq"
    url = "https://cpan.metacpan.org/authors/id/B/BL/BLAINEM/List-Uniq-0.23.tar.gz"

    maintainers("EbiArnie")

    version("0.23", sha256="71d8bee467e4669cd8f891b0acdd6332bb9efcdb9046bf4694bf76325b618d6d")


    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
