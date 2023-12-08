# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlRoseDb(PerlPackage):
    """A DBI wrapper and abstraction layer."""

    homepage = "https://metacpan.org/pod/Rose::DB"
    url = "https://cpan.metacpan.org/authors/id/J/JS/JSIRACUSA/Rose-DB-0.785.tar.gz"

    maintainers("EbiArnie")

    version("0.785", sha256="7849307d748d9672b42ef3cd78f83d44dec034cdc94f4d4251d2761e27c67a3c")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))
    depends_on("perl-bit-vector", type=("run"))
    depends_on("perl-clone-pp", type=("run"))
    depends_on("perl-datetime", type=("run"))
    depends_on("perl-datetime-format-mysql", type=("run"))
    depends_on("perl-datetime-format-oracle", type=("run"))
    depends_on("perl-datetime-format-pg@0.11:", type=("run"))
    depends_on("perl-dbi", type=("run"))
    depends_on("perl-rose-datetime", type=("run"))
    depends_on("perl-rose-object@0.854:", type=("run"))
    depends_on("perl-sql-reservedwords", type=("run"))
    depends_on("perl-time-clock", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
