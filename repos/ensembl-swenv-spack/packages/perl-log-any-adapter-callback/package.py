# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlLogAnyAdapterCallback(PerlPackage):
    """(DEPRECATED)(ADOPTME) Send Log::Any logs to a subroutine"""

    homepage = "https://metacpan.org/pod/Log::Any::Adapter::Callback"
    url = "https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Log-Any-Adapter-Callback-0.102.tar.gz"

    maintainers("EbiArnie")

    version("0.102", sha256="7c01883265bdab65344257c1b1d1e69fbe300e7693dddeebb98f9f67310e07cd")

    depends_on("perl-log-any", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
