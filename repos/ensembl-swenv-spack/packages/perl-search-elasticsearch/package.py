# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlSearchElasticsearch(PerlPackage):
    """The official client for Elasticsearch"""

    homepage = "https://metacpan.org/pod/Search::Elasticsearch"
    url = "https://cpan.metacpan.org/authors/id/E/EZ/EZIMUEL/Search-Elasticsearch-8.00.tar.gz"

    maintainers("EbiArnie")

    version("8.00", sha256="4b95357072b7432e02cc9ef897881976650e03030c15ec752789299284ce30ab")

    depends_on("perl-any-uri-escape", type=("run"))
    depends_on("perl-devel-globaldestruction", type=("run"))
    depends_on("perl-http-message", type=("run"))
    depends_on("perl-io-socket-ssl", type=("test"))
    depends_on("perl-json-maybexs@1.002002:", type=("run"))
    depends_on("perl-libwww-perl", type=("run"))
    depends_on("perl-log-any@1.02:", type=("run"))
    depends_on("perl-log-any-adapter-callback@0.09:", type=("test"))
    depends_on("perl-module-runtime", type=("run"))
    depends_on("perl-moo@2.001000:", type=("run"))
    depends_on("perl-namespace-clean", type=("run"))
    depends_on("perl-net-ip", type=("run"))
    depends_on("perl-package-stash@0.34:", type=("run"))
    depends_on("perl-sub-exporter", type=("run"))
    depends_on("perl-test-deep", type=("test"))
    depends_on("perl-test-exception", type=("test"))
    depends_on("perl-test-pod", type=("test"))
    depends_on("perl-test-sharedfork", type=("test"))
    depends_on("perl-try-tiny", type=("run"))
    depends_on("perl-uri", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
