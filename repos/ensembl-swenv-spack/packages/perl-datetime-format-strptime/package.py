# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDatetimeFormatStrptime(PerlPackage):
    """Parse and format strp and strf time patterns"""

    homepage = "https://metacpan.org/pod/DateTime::Format::Strptime"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Strptime-1.79.tar.gz"

    maintainers("EbiArnie")

    version("1.79", sha256="701e46802c86ed4d88695c1a6dacbbe90b3390beeb794f387e7c792300037579")

    depends_on("perl-datetime@1.00:", type=("run"))
    depends_on("perl-datetime-locale@1.30:", type=("run"))
    depends_on("perl-datetime-timezone@2.09:", type=("run"))
    depends_on("perl-params-validationcompiler", type=("run"))
    depends_on("perl-specio@0.33:", type=("run"))
    depends_on("perl-test-fatal", type=("test"))
    depends_on("perl-test-warnings", type=("test"))
    depends_on("perl-try-tiny", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
