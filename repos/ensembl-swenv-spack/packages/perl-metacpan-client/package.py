# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlMetacpanClient(PerlPackage):
    """A comprehensive, DWIM-featured client to the MetaCPAN API"""

    homepage = "https://metacpan.org/pod/MetaCPAN::Client"
    url = "https://cpan.metacpan.org/authors/id/M/MI/MICKEY/MetaCPAN-Client-2.031000.tar.gz"

    maintainers("EbiArnie")

    version("2.031000", sha256="c6ceaf886a74120e2bffe2ec1f09d0fdc330acbfdb9ec876ef925ee687ec7cf5")

    depends_on("perl@5.10.0:", type=("build", "link", "run", "test"))
    depends_on("perl-io-socket-ssl@1.42:", type=("run"))
    depends_on("perl-json-maybexs", type=("run"))
    depends_on("perl-lwp-protocol-https", type=("test"))
    depends_on("perl-moo", type=("run"))
    depends_on("perl-net-ssleay@1.49:", type=("run"))
    depends_on("perl-ref-util", type=("run"))
    depends_on("perl-safe-isa", type=("run"))
    depends_on("perl-test-fatal", type=("test"))
    depends_on("perl-test-needs@0.002005:", type=("test"))
    depends_on("perl-type-tiny", type=("run"))
    depends_on("perl-uri", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
