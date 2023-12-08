# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlRefUtil(PerlPackage):
    """Utility functions for checking references"""

    homepage = "https://metacpan.org/pod/Ref::Util"
    url = "https://cpan.metacpan.org/authors/id/A/AR/ARC/Ref-Util-0.204.tar.gz"

    maintainers("EbiArnie")

    version("0.204", sha256="415fa73dbacf44f3d5d79c14888cc994562720ab468e6f71f91cd1f769f105e1")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
