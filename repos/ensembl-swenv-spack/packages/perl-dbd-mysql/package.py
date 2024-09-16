# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import inspect
import subprocess
from spack.package import *

class PerlDbdMysql(PerlPackage):
    """MySQL driver for the Perl5 Database Interface (DBI)"""

    homepage = "https://metacpan.org/pod/DBD::mysql"
    url = "https://cpan.metacpan.org/authors/id/D/DV/DVEEDEN/DBD-mysql-4.050.tar.gz"

    version("4.052", sha256="a83f57af7817787de0ef56fb15fdfaf4f1c952c8f32ff907153b66d2da78ff5b")
    version("4.050", sha256="4f48541ff15a0a7405f76adc10f81627c33996fbf56c95c26c094444c0928d78")
    version("4.043", sha256="629f865e8317f52602b2f2efd2b688002903d2e4bbcba5427cb6188b043d6f99")

    requires("%gcc")

    depends_on("perl-test-deep", type=("build", "run"))
    depends_on("perl-dbi", type=("build", "run"))
    # Avoid segfault with 8.0.33 and DBD::mysql 4.050
    # See https://github.com/perl5-dbi/DBD-mysql/issues/352
    depends_on("mysql@:8.0.32", type=("build", "link", "run"))
    depends_on("openssl", type=("build", "link", "run"))
    depends_on("perl-devel-checklib", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))

#    def configure_args(self):
#        conf_binary = join_path(self.spec["mysql"].prefix.bin, "mysql_config")
#        libs = subprocess.check_output([conf_binary, "--libs"])
#        libs = libs.decode('utf-8')
#        libs = libs.rstrip()
#        cflags = subprocess.check_output([conf_binary, "--cflags"])
#        cflags = cflags.decode('utf-8')
#        cflags = cflags.rstrip()
#        for lib in [
#                self.spec["openssl"].libs.ld_flags,
#                self.spec["zlib"].libs.ld_flags
#                ]:
#            libs = lib + ' '+ libs
#        # run mysql_config -cflags. 
#        for flag in [
#                '-Wl,-rpath,' + self.spec["openssl"].prefix.lib,
#                '-Wl,-rpath,' + self.spec["zlib"].prefix.lib,
#                self.spec["openssl"].headers.include_flags,
#                self.spec["zlib"].headers.include_flags
#                ]:
#            cflags = flag + ' ' + cflags
#
#        ldflags = ''
#        for flag in [
#                '-Wl,-rpath,' + self.spec["openssl"].prefix.lib,
#                '-Wl,-rpath,' + self.spec["zlib"].prefix.lib,
#                ]:
#            ldflags = flag + ' ' + ldflags
#
#        return ['--cflags=' + cflags, '--libs=' + libs, '--ldflags=' + ldflags]
