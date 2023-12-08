# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDatetimeFormatPg(PerlPackage):
    """Parse and format PostgreSQL dates and times"""

    homepage = "https://metacpan.org/pod/DateTime::Format::Pg"
    url = "https://cpan.metacpan.org/authors/id/D/DM/DMAKI/DateTime-Format-Pg-0.16014.tar.gz"

    maintainers("EbiArnie")

    version("0.16014", sha256="38bb9666524dc384c3366f6342cb9656c50bac0f9716a3d44f1cf552ccbe0eb9")

    depends_on("perl-datetime@0.10:", type=("run"))
    depends_on("perl-datetime-format-builder@0.72:", type=("run"))
    depends_on("perl-datetime-timezone@0.05:", type=("run"))
    depends_on("perl-module-build-tiny@0.035:", type=("build"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
