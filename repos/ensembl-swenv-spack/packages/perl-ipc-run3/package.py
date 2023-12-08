# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlIpcRun3(PerlPackage):
    """Run a subprocess with input/ouput redirection"""

    homepage = "https://metacpan.org/pod/IPC::Run3"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IPC-Run3-0.048.tar.gz"

    maintainers("EbiArnie")

    version("0.048", sha256="3d81c3cc1b5cff69cca9361e2c6e38df0352251ae7b41e2ff3febc850e463565")


    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
