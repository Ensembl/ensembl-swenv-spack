# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDatetimeFormatMysql(PerlPackage):
    """Parse and format MySQL dates and times"""

    homepage = "https://metacpan.org/pod/DateTime::Format::MySQL"
    url = "https://cpan.metacpan.org/authors/id/X/XM/XMIKEW/DateTime-Format-MySQL-0.08.tar.gz"

    maintainers("EbiArnie")

    version("0.08", sha256="19cb70e98584655e354d2d6a8e71cc5ca902dddc3ac44416712f9163d122b9e8")

    depends_on("perl-datetime", type=("run"))
    depends_on("perl-datetime-format-builder@0.6:", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
