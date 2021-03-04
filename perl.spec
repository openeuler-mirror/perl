%global perl_libdir %{_libdir}/perl5
%global perl_datadir %{_datadir}/perl5
%global perl_vendor_libdir  %{perl_libdir}/vendor_perl
%global perl_vendor_datadir %{perl_datadir}/vendor_perl
%global perl_new LD_PRELOAD="%{buildroot}%{perl_libdir}/CORE/libperl.so" \
    LD_LIBRARY_PATH="%{buildroot}%{perl_libdir}/CORE" \
    PERL5LIB="%{buildroot}%{perl_libdir}:%{buildroot}%{perl_datadir}" \
    %{buildroot}%{_bindir}/%{name}

#remove autofind requires and provides of {_libexecdir}/perl5-tests/
%global __provides_exclude_from ^%{_libexecdir}/perl5-tests/.*$
%global __requires_exclude_from ^%{_libexecdir}/perl5-tests/.*$

#provides module without verion, no need to provide
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((charnames|DynaLoader|DB)\\)$

%global perl_version 5.32.0

%global perl_compat perl(:MODULE_COMPAT_5.32.0)

Name:           perl
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic) and MIT and UCD and Public Domain and BSD
Epoch:          4
Version:        %{perl_version}
Release:        3
Summary:        A highly capable, feature-rich programming language
Url:            https://www.perl.org/
Source0:        https://www.cpan.org/src/5.0/%{name}-%{version}.tar.xz

# PATCH-FEATURE-OPENEULER
Patch1:         change-lib-to-lib64.patch
# PATCH-FEATURE-OPENEULER
Patch2:         disable-rpath-by-default.patch
# PATCH-FIX-OPENEULER
Patch3:         create-libperl-soname.patch
# PATCH-FIX-OPENEULER--rh#1107543, RT#61912
Patch4:         perl-5.18.2-Destroy-GDBM-NDBM-ODBM-SDBM-_File-objects-only-from-.patch

BuildRequires:  gcc bash findutils coreutils make tar procps bzip2-devel gdbm-devel
BuildRequires:  zlib-devel systemtap-sdt-devel perl-interpreter perl-generators gdb

Requires:       perl-libs = %{epoch}:%{version}-%{release}
Requires:       perl-version perl-threads perl-threads-shared perl-parent
Requires:       perl-devel = %{epoch}:%{version}-%{release} system-rpm-config
Requires:       perl-Unicode-Collate perl-Unicode-Normalize perl-Time-Local perl-Time-HiRes
Requires:       perl-Thread-Queue perl-Text-Tabs+Wrap perl-Test-Simple perl-Test-Harness perl-devel
Requires:       perl-Text-Balanced perl-Text-ParseWords perl-Term-ANSIColor perl-Term-Cap
Requires:       perl-Socket perl-podlators perl-Scalar-List-Utils perl-perlfaq perl-constant
Requires:       perl-Digest-SHA perl-Digest perl-Digest-MD5 perl-Devel-PPPort perl-Carp perl-Env
Requires:       perl-CPAN-Meta-Requirements  perl-CPAN-Meta perl-CPAN-Meta-YAML perl-ExtUtils-Command
Requires:       perl-ExtUtils-Install perl-ExtUtils-Manifest perl-ExtUtils-MakeMaker perl-ExtUtils-ParseXS
Requires:       perl-File-Fetch perl-File-Path perl-File-Temp perl-Filter-Simple perl-Filter perl-Encode
Requires:       perl-IO-Compress perl-IO-Socket-IP perl-autodie perl-bignum perl-B-Debug perl-encoding
Requires:       perl-Exporter perl-experimental perl-Compress-Raw-Bzip2 perl-Compress-Raw-Zlib perl-HTTP-Tiny
Requires:       perl-Locale-Codes perl-Locale-Maketext perl-Math-BigInt perl-Math-BigInt-FastCalc perl-Math-BigRat
Requires:       perl-Archive-Tar perl-Config-Perl-V perl-Data-Dumper perl-DB_File perl-Getopt-Long perl-libnet
Requires:       perl-IPC-Cmd perl-IPC-SysV perl-JSON-PP perl-MIME-Base64 perl-Params-Check perl-Storable
Requires:       perl-Pod-Checker perl-Pod-Escapes perl-Pod-Parser perl-Pod-Perldoc perl-Pod-Simple perl-Pod-Usage
Requires:       perl-Module-CoreList perl-Module-CoreList-tools perl-Module-Load perl-Module-Load-Conditional
Requires:       perl-Module-Metadata perl-Sys-Syslog perl-PerlIO-via-QuotedPrint perl-Perl-OSType

Provides:       perl-Attribute-Handlers perl-interpreter perl(bytes_heavy.pl) perl(dumpvar.pl) perl(perl5db.pl)
Provides:       perl-ExtUtils-Embed perl-ExtUtils-Miniperl perl-IO perl-IO-Zlib perl-Locale-Maketext-Simple perl-Math-Complex
Provides:       perl-Module-Loaded perl-Net-Ping perl-Pod-Html perl-SelfLoader perl-Test perl-Time-Piece perl-libnetcfg perl-open perl-utils
Provides:       perl-Errno perl-Memoize

Obsoletes:      perl-Attribute-Handlers perl-interpreter perl-Errno perl-ExtUtils-Embed perl-Net-Ping
Obsoletes:      perl-ExtUtils-Miniperl perl-IO perl-IO-Zlib perl-Locale-Maketext-Simple perl-Math-Complex perl-Memoize perl-Module-Loaded
Obsoletes:      perl-Pod-Html perl-SelfLoader perl-Test perl-Time-Piece perl-libnetcfg perl-open perl-utils


%description
Perl 5 is a highly capable, feature-rich programming language with over 30 years of development.
Perl 5 runs on over 100 platforms from portables to mainframes and is suitable for both rapid
prototyping and large scale development projects.

%package libs
Summary:        The libraries for the perl
License:        (GPL+ or Artistic) and HSRL and MIT and UCD
Provides:       perl(:MODULE_COMPAT_5.28.0) perl(:VERSION) = 5.28.0
Provides:       %perl_compat
Provides:       perl(:VERSION) = %{perl_version} libperl.so.5.28()(64bit)
Provides:       perl(:WITH_64BIT) perl(:WITH_ITHREADS) perl(:WITH_THREADS)
Provides:       perl(:WITH_LARGEFILES) perl(:WITH_PERLIO) perl(unicore::Name)
Provides:       perl(utf8_heavy.pl)
Requires:       perl(Carp) perl(Exporter) perl(XSLoader)

%description libs
This package is the shared library for perl.

%package devel
Summary:        Development files for %{name}
License:        (GPL+ or Artistic) and UCD

Requires:       perl = %{epoch}:%{version}-%{release} system-rpm-config systemtap-sdt-devel
Requires:       perl(ExtUtils::ParseXS) perl(:MODULE_COMPAT_5.28.0) perl(Devel::PPPort)

Provides:       perl-Devel-Peek perl-Devel-SelfStubber perl-tests

Obsoletes:      perl-Devel-Peek perl-Devel-SelfStubber perl-tests

%description devel
This package contains the development files and test files for %{name}.

%package_help

%prep
%autosetup -n %{name}-%{perl_version} -p1
%global perl_abi   %(echo '%{perl_version}' | sed 's/^\\([^.]*\\.[^.]*\\).*/\\1/') 
echo %{perl_abi}

# Configure Compress::Zlib to use system zlib
sed -i 's|BUILD_ZLIB      = True|BUILD_ZLIB      = False|
    s|INCLUDE         = ./zlib-src|INCLUDE         = %{_includedir}|
    s|LIB             = ./zlib-src|LIB             = %{_libdir}|' \
    cpan/Compress-Raw-Zlib/config.in

rm -rf cpan/Compress-Raw-Zlib/zlib-src
rm -rf cpan/Compress-Raw-Bzip2/bzip2-src
sed -i '/\(bzip2\|zlib\)-src/d' MANIFEST

%build
/bin/sh Configure -des -Doptimize="none" -Dccflags="$RPM_OPT_FLAGS" \
        -Dldflags="$RPM_LD_FLAGS" -Dccdlflags="-Wl,--enable-new-dtags $RPM_LD_FLAGS" \
        -Dlddlflags="-shared $RPM_LD_FLAGS" -Dshrpdir="%{_libdir}" \
        -DDEBUGGING=-g -Dversion=%{version} -Dmyhostname=localhost \
        -Dperladmin=root@localhost -Dcc='%{__cc}' -Dprefix=%{_prefix} \
        -Dvendorprefix=%{_prefix} -Dsiteprefix=%{_prefix}/local \
        -Dsitelib="%{_prefix}/local/share/perl5" -Dprivlib="%{perl_datadir}" \
        -Dsitearch="%{_prefix}/local/%{_lib}/perl5" \
        -Dvendorlib="%{perl_vendor_datadir}" -Darchlib="%{perl_libdir}" \
        -Dvendorarch="%{perl_vendor_libdir}" -Darchname="%{_arch}-%{_os}-thread-multi" \
        -Dlibpth="/usr/local/lib64 /lib64 %{_prefix}/lib64" \
        -Duseshrplib -Dusethreads -Duseithreads -Ui_ndbm -Di_gdbm \
        -Dusedtrace='/usr/bin/dtrace' -Ubincompat5005 -Dusesitecustomize \
        -Duselargefiles -Dd_semctl_semun -Di_db -Duse64bitint \
        -Di_shadow -Di_syslog -Dman3ext=3pm -Duseperlio -Dscriptdir='%{_bindir}' \
        -Dinstallusrbinperl=n -Uversiononly -Dpager='/usr/bin/less -isr' \
        -Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_sethostent_r_proto \
        -Ud_endprotoent_r_proto -Ud_setprotoent_r_proto \
        -Ud_endservent_r_proto -Ud_setservent_r_proto \

BUILD_BZIP2=0
BZIP2_LIB=%{_libdir}
export BUILD_BZIP2 BZIP2_LIB

# for new perl can be executed from make.
%global soname libperl.so.%{perl_abi}
test -L %{soname} || ln -s libperl.so %{soname}

make %{?_smp_mflags}

%install
%make_install
# move libperl to standard path.
mv "%{buildroot}%{perl_libdir}/CORE/libperl.so" "%{buildroot}%{_libdir}/libperl.so.%{version}"
ln -s "libperl.so.%{version}" "%{buildroot}%{_libdir}/%{soname}"
ln -s "libperl.so.%{version}" "%{buildroot}%{_libdir}/libperl.so"
# Keep symlink from original location
ln -s "../../libperl.so.%{version}" "%{buildroot}%{perl_libdir}/CORE/libperl.so"

rm -f "%{buildroot}%{perl_libdir}/CORE/%{soname}"

install -p -m 755 utils/pl2pm %{buildroot}%{_bindir}/pl2pm

for h_file in sys/ioctl.h sys/syscall.h syscall.h
do
    %{perl_new} %{buildroot}%{_bindir}/h2ph -a -d %{buildroot}%{perl_libdir} $h_file || true
done

mkdir -p %{buildroot}%{perl_vendor_libdir}/auto
mkdir -p %{buildroot}%{perl_vendor_datadir}

# This is a work-around for rpmbuild bug #878863.
find %{buildroot} -type f -name '*.bs' -empty -delete
chmod -R u+w %{buildroot}/*

rm %{buildroot}%{perl_datadir}/ExtUtils/xsubpp
ln -s ../../../bin/xsubpp %{buildroot}%{perl_datadir}/ExtUtils/

rm %{buildroot}%{perl_libdir}/.packlist

# bug #973713
rm %{buildroot}/%{perl_libdir}/File/Spec/VMS.pm
rm %{buildroot}%{_mandir}/man3/File::Spec::VMS.3*

# tests
mkdir -p %{buildroot}%{_libexecdir}/perl5-tests/perl-tests
tar -cf - t/ | ( cd %{buildroot}%{_libexecdir}/perl5-tests/perl-tests && tar -xf - )
for dir in `find ext/ -type d -name t -maxdepth 2` ; do
    tar -cf - $dir | ( cd %{buildroot}%{_libexecdir}/perl5-tests/perl-tests/t && tar -xf - )
done

# fix shell bangs in tests.
%{perl_new} -MConfig -i -pn \
    -e 's"\A#!(?:perl|\./perl|/perl|/usr/bin/perl|/usr/bin/env perl)\b"$Config{startperl}"' \
    $(find %{buildroot}%{_libexecdir}/perl5-tests/perl-tests -type f)

%check
%{perl_new} -I/lib regen/lib_cleanup.pl
pushd t
%{perl_new} -I../lib porting/customized.t --regen
popd
TEST_JOBS=$(echo %{?_smp_mflags} | sed 's/.*-j\([0-9][0-9]*\).*/\1/') \
LC_ALL=C make test_harness

%ldconfig_scriptlets

%files
# there are many files do not need to be packaged
# in this main package
%exclude %{_bindir}/{h2xs,perlivp,corelist,prove,cpan,enc2xs,streamzip}
%exclude %{_bindir}/{ptar,ptargrep,ptardiff,shasum,json_pp}
%exclude %{_bindir}/{encguess,piconv,instmodsh,xsubpp,pod2text}
%exclude %{_bindir}/{podchecker,podselect,perldoc,pod2usage,pod2man}
%exclude %dir %{perl_datadir}/Archive
%exclude %{perl_libdir}/CORE/*.h
%exclude %{perl_datadir}/Archive/{Tar,Tar.pm}
%exclude %{perl_datadir}/autodie/
%exclude %{perl_datadir}/{autodie.pm,Fatal.pm}
%exclude %{perl_datadir}/B/Debug.pm
%exclude %{perl_datadir}/{Carp,Carp.*}
%exclude %{perl_datadir}/Config/Perl
%exclude %{perl_datadir}/constant.pm
%exclude %dir %{perl_datadir}/App
%exclude %{perl_datadir}/App/Cpan.pm
%exclude %{perl_datadir}/{CPAN,CPAN.pm}
%exclude %dir %{perl_datadir}/{CPAN,CPAN/Meta,CPAN/Meta/History,Parse,Parse/CPAN}
%exclude %{perl_datadir}/CPAN/Meta.pm
%exclude %{perl_datadir}/CPAN/Meta/{Converter.pm,Feature.pm,History.pm}
%exclude %{perl_datadir}/CPAN/Meta/{Merge.pm,Prereqs.pm,Spec.pm,Validator.pm}
%exclude %{perl_datadir}/Parse/CPAN/Meta.pm
%exclude %{perl_datadir}/CPAN/Meta/Requirements.pm
%exclude %{perl_datadir}/CPAN/Meta/YAML.pm
%exclude %dir %{perl_libdir}/{Compress,Compress/Raw}
%exclude %dir %{perl_libdir}/{auto/Compress,auto/Compress/Raw}
%exclude %{perl_libdir}/Compress/Raw/Bzip2.pm
%exclude %{perl_libdir}/auto/Compress/Raw/Bzip2
%exclude %{perl_libdir}/Compress/Raw/Zlib.pm
%exclude %{perl_libdir}/auto/Compress/Raw/Zlib
%exclude %dir %{perl_libdir}/auto/Data
%exclude %dir %{perl_libdir}/auto/Data/Dumper
%exclude %{perl_libdir}/auto/Data/Dumper/Dumper.so
%exclude %dir %{perl_libdir}/Data
%exclude %{perl_libdir}/Data/Dumper.pm
%exclude %{perl_libdir}/DB_File.pm
%exclude %dir %{perl_libdir}/auto/DB_File
%exclude %{perl_libdir}/auto/DB_File/DB_File.so
%dir %exclude %{perl_libdir}/Devel
%exclude %{perl_libdir}/Devel/Peek.pm
%dir %exclude %{perl_libdir}/auto/Devel
%exclude %{perl_libdir}/auto/Devel/Peek
%exclude %{perl_libdir}/Devel/PPPort.pm
%exclude %dir %{perl_datadir}/Devel
%exclude %{perl_datadir}/Devel/SelfStubber.pm
%exclude %{perl_datadir}/Digest.pm
%exclude %dir %{perl_datadir}/Digest
%exclude %{perl_datadir}/Digest/{base.pm,file.pm}
%exclude %dir %{perl_libdir}/Digest
%exclude %{perl_libdir}/Digest/MD5.pm
%exclude %dir %{perl_libdir}/auto/Digest
%exclude %{perl_libdir}/auto/Digest/MD5
%exclude %{perl_libdir}/Digest/SHA.pm
%exclude %{perl_libdir}/auto/Digest/SHA
%exclude %{perl_libdir}/Encode*
%exclude %{perl_libdir}/auto/Encode*
%exclude %{perl_datadir}/Encode
%exclude %{perl_libdir}/encoding.pm
%exclude %dir %{perl_datadir}/Encode
%exclude %{perl_datadir}/Encode/{*.e2x,encode.h}
%exclude %{perl_datadir}/Env.pm
%exclude %{perl_datadir}/Exporter*
%exclude %{perl_datadir}/experimental*
%exclude %{perl_datadir}/ExtUtils/{CBuilder,CBuilder.pm}
%exclude %{perl_datadir}/ExtUtils/Command.pm
%exclude %{perl_datadir}/ExtUtils/{Install.pm,Installed.pm,Packlist.pm}
%exclude %{perl_datadir}/ExtUtils/{Manifest.pm,MANIFEST.SKIP}
%exclude %{perl_datadir}/ExtUtils/{Command,Liblist,Liblist.pm,MM.pm}
%exclude %{perl_datadir}/ExtUtils/{MakeMaker,MakeMaker.pm,MM_*.pm,MY.pm}
%exclude %{perl_datadir}/ExtUtils/{Mkbootstrap.pm,Mksymlists.pm,testlib.pm}
%exclude %dir %{perl_datadir}/ExtUtils/MM
%exclude %{perl_datadir}/ExtUtils/MM/Utils.pm
%exclude %dir %{perl_datadir}/ExtUtils/ParseXS
%exclude %{perl_datadir}/ExtUtils/{ParseXS.pm,ParseXS.pod}
%exclude %{perl_datadir}/ExtUtils/ParseXS/{Constants.pm,CountLines.pm}
%exclude %{perl_datadir}/ExtUtils/ParseXS/{Utilities.pm,Eval.pm}
%exclude %dir %{perl_datadir}/ExtUtils/Typemaps
%exclude %{perl_datadir}/ExtUtils/{Typemaps.pm,xsubpp}
%exclude %{perl_datadir}/ExtUtils/Typemaps/{Cmd.pm,InputMap.pm}
%exclude %{perl_datadir}/ExtUtils/Typemaps/{OutputMap.pm,Type.pm}
%exclude %{perl_datadir}/File/{Fetch.pm,Path.pm,Temp.pm}
%exclude %dir %{perl_libdir}/auto/Filter
%exclude %{perl_libdir}/auto/Filter/Util
%exclude %dir %{perl_libdir}/Filter
%exclude %{perl_libdir}/Filter/Util
%exclude %{perl_datadir}/pod/perlfilter.pod
%exclude %dir %{perl_datadir}/Filter
%exclude %{perl_datadir}/Filter/Simple.pm
%exclude %{_bindir}/zipdetails
%exclude %dir %{perl_datadir}/IO/Compress
%exclude %{perl_datadir}/IO/Compress/FAQ.pod
%exclude %{perl_datadir}/Getopt/Long.pm
%exclude %dir %{perl_datadir}/Compress
%exclude %{perl_datadir}/Compress/Zlib.pm
%exclude %{perl_datadir}/File/GlobMapper.pm
%exclude %{perl_datadir}/IO/Compress/{Base,Base.pm}
%exclude %dir %{perl_datadir}/IO/Uncompress
%exclude %{perl_datadir}/IO/Uncompress/{AnyUncompress.pm,Base.pm}
%exclude %{perl_datadir}/IO/Compress/{Adapter,Gzip,Zip,Zlib}
%exclude %{perl_datadir}/IO/Compress/{Deflate.pm,Gzip.pm,Zip.pm}
%exclude %{perl_datadir}/IO/Compress/{RawDeflate.pm,Bzip2.pm}
%exclude %{perl_datadir}/IO/Uncompress/{Adapter,AnyInflate.pm}
%exclude %{perl_datadir}/IO/Uncompress/{Bunzip2.pm,Gunzip.pm,Unzip.pm}
%exclude %{perl_datadir}/IO/Uncompress/{Inflate.pm,RawInflate.pm}
%exclude %dir %{perl_datadir}/IO/Socket
%exclude %{perl_datadir}/IO/Socket/IP.pm
%exclude %dir %{perl_datadir}/HTTP
%exclude %{perl_datadir}/HTTP/Tiny.pm
%exclude %{perl_libdir}/Time/HiRes.pm
%exclude %{perl_libdir}/auto/Time/HiRes
%exclude %{perl_datadir}/Time/Local.pm
%exclude %{perl_datadir}/Thread/Queue.pm
%exclude %{perl_libdir}/List/
%exclude %{perl_libdir}/Scalar/
%exclude %{perl_libdir}/Sub/
%exclude %{perl_libdir}/auto/List/
%exclude %{perl_libdir}/Storable.pm
%exclude %{perl_libdir}/Sys/Syslog.pm
%exclude %{perl_datadir}/Term/ANSIColor.pm
%exclude %{perl_datadir}/Term/Cap.pm
%exclude %{perl_libdir}/auto/Sys/Syslog/
%exclude %{perl_libdir}/auto/Storable/
%exclude %{perl_datadir}/IPC/Cmd.pm
%exclude %{perl_libdir}/auto/IPC
%exclude %{perl_libdir}/IPC/{Msg.pm,Semaphore.pm,SysV.pm,SharedMem.pm}
%exclude %dir %{perl_datadir}/JSON
%exclude %{perl_datadir}/JSON/{PP,PP.pm}
%exclude %{perl_datadir}/Net/{Cmd.pm,Time.pm,SMTP.pm,POP3.pm,Netrc.pm,FTP}
%exclude %{perl_datadir}/Net/{Config.pm,NNTP.pm,libnetFAQ.pod,FTP.pm,Domain.pm}
%exclude %{perl_datadir}/Locale/{Codes,Codes.*,Script.*,Maketext.*}
%exclude %{perl_datadir}/Locale/{Country.*,Currency.*,Language.*}
%exclude %{perl_datadir}/Locale/Maketext/{Cookbook.*,Guts.*}
%exclude %{perl_datadir}/Locale/Maketext/{GutsLoader.*,TPJ13.*}
%exclude %{perl_datadir}/big*.pm
%exclude %{perl_datadir}/Math/BigFloat
%exclude %{perl_datadir}/Math/{BigFloat.pm,BigInt.pm,BigRat.pm}
%exclude %dir %{perl_datadir}/Math/BigInt
%exclude %{perl_datadir}/Math/BigInt/{Calc.pm,CalcEmu.pm,Lib.pm,Trace.pm}
%exclude %{perl_libdir}/Math
%exclude %{perl_libdir}/auto/Math
%exclude %{perl_libdir}/auto/MIME
%exclude %{perl_libdir}/MIME
%exclude %{perl_datadir}/Module/{CoreList,Load,CoreList.pm,CoreList.pod,Load.pm,Metadata.pm}
%exclude %{perl_libdir}/Cwd.pm
%exclude %{perl_libdir}/File/Spec*
%exclude %{perl_libdir}/auto/Cwd/
%exclude %{perl_datadir}/Params/
%exclude %{perl_datadir}/perlfaq.pm
%exclude %{perl_datadir}/pod/{perlfaq*,perlglossary.pod}
%exclude %{perl_datadir}/PerlIO
%exclude %dir %{perl_datadir}/Perl
%exclude %{perl_datadir}/Perl/OSType.pm
%exclude %{perl_datadir}/parent.pm
%exclude %{perl_datadir}/pod/{perldoc.pod,perlpodstyle.pod}
%exclude %{perl_datadir}/Pod/{Checker.pm,Escapes.pm,Find.pm,Select.pm}
%exclude %{perl_datadir}/Pod/{InputObjects.pm,ParseUtils.pm,Parser.pm,PlainText.pm}
%exclude %{perl_datadir}/Pod/{Perldoc.pm,Usage.pm,Man.pm}
%exclude %{perl_datadir}/Pod/Perldoc/
%exclude %{perl_datadir}/Pod/Simple/
%exclude %{perl_datadir}/Pod/{ParseLink.pm,Text,Text.pm,Simple.pm,Simple.pod}
%exclude %dir %{perl_datadir}/App
%exclude %{perl_datadir}/App/Prove*
%exclude %dir %{perl_libdir}/auto/{Socket,threads}
%exclude %{perl_libdir}/auto/Socket/Socket.*
%exclude %{perl_libdir}/auto/threads/{threads*,shared*}
%exclude %{perl_libdir}/{threads.pm,Socket.pm}
%exclude %dir %{perl_libdir}/threads
%exclude %{perl_libdir}/threads/shared*
%dir %exclude %{perl_libdir}/auto/Unicode
%exclude %{perl_libdir}/auto/Unicode/{Collate,Normalize}
%dir %exclude %{perl_libdir}/Unicode
%exclude %{perl_libdir}/Unicode/Collate
%exclude %{perl_libdir}/Unicode/{Collate.pm,Normalize.pm}
%exclude %{perl_datadir}/Unicode/Collate
%exclude %{perl_datadir}/{TAP*,ok*,Test2*}
%exclude %dir %{perl_datadir}/Test
%exclude %{perl_datadir}/Test/{Harness*,More*,Builder*,use}
%exclude %{perl_datadir}/Test/{Tester*,Simple*,Tutorial*}
%exclude %{perl_datadir}/Text/{Balanced.pm,ParseWords.pm}
%exclude %{perl_datadir}/Text/{Tabs.pm,Wrap.pm}
%exclude %{perl_datadir}/{version.pm,version.pod}
%exclude %{perl_datadir}/version/

#libs
%exclude %dir %{perl_libdir}
%exclude %dir %{perl_libdir}/auto
%exclude %{perl_libdir}/auto/re
%exclude %dir %{perl_libdir}/CORE
%exclude %{perl_libdir}/CORE/libperl.so
%exclude %{perl_libdir}/re.pm
%exclude %{_libdir}/libperl.so.*
%exclude %dir %{perl_vendor_libdir}
%exclude %dir %{perl_vendor_libdir}/auto
%exclude %dir %{perl_datadir}
%exclude %{perl_datadir}/{integer.pm,strict.pm,unicore,utf8.pm}
%exclude %{perl_datadir}/{utf8_heavy.pl,warnings.pm,XSLoader.pm}
%exclude %dir %{perl_vendor_datadir}

%license Artistic Copying
%doc AUTHORS
%{_bindir}/*
%dir %{perl_libdir}
%{perl_libdir}/*
%dir %{perl_datadir}
%{perl_datadir}/*

%files libs
%license Artistic Copying
%doc AUTHORS README Changes
%dir %{perl_libdir}
%dir %{perl_libdir}/auto
%{perl_libdir}/auto/re
%dir %{perl_libdir}/CORE
%{perl_libdir}/CORE/libperl.so
%{perl_libdir}/re.pm
%{_libdir}/libperl.so.*
%dir %{perl_vendor_libdir}
%dir %{perl_vendor_libdir}/auto
%dir %{perl_datadir}
%{perl_datadir}/{integer.pm,strict.pm,unicore,utf8.pm}
%{perl_datadir}/{utf8_heavy.pl,warnings.pm,XSLoader.pm}
%dir %{perl_vendor_datadir}

%files devel
%{_bindir}/{h2xs,perlivp}
%{perl_libdir}/CORE/*.h
%{_libdir}/libperl.so
%dir %{perl_libdir}/Devel
%{perl_libdir}/Devel/Peek.pm
%dir %{perl_libdir}/auto/Devel
%{perl_libdir}/auto/Devel/Peek
%dir %{perl_datadir}/Devel
%{perl_datadir}/Devel/SelfStubber.pm
%{_libexecdir}/perl5-tests/

%files help
# there are many man docs don not need to be packaged
%exclude %{_mandir}/man1/{ptar.1*,ptardiff.1*,ptargrep.1*,cpan.1*,shasum.1*,perlfilter.*}
%exclude %{_mandir}/man1/{encguess.1*,piconv.1*,enc2xs.1*,instmodsh.1*,xsubpp*,podchecker.*}
%exclude %{_mandir}/man1/{zipdetails.*,json_pp.1*,corelist*,perlfaq*,perlglossary.*,streamzip.*}
%exclude %{_mandir}/man1/{podselect.1*,perldoc.1*,pod2usage.*,pod2man.1*,pod2text.1*}
%exclude %{_mandir}/man1/{perlpodstyle.1*,prove.1*}
%exclude %{_mandir}/man3/{Archive::Tar*,autodie*,Fatal.3*,B::Debug.3*,Pod::Find.*}
%exclude %{_mandir}/man3/{big*.*,Carp.*,Config::Perl::V.*,constant.3*,Pod::InputObjects.*}
%exclude %{_mandir}/man3/{App::Cpan.*,*CPAN*,Compress::Raw::*,Data::Dumper.3*,Pod::ParseUtils.*}
%exclude %{_mandir}/man3/{Digest*,DB_File*,Encode*.3*,encoding.3*,Env.3*,Exporter*,Pod::Parser.*}
%exclude %{_mandir}/man3/{experimental*,ExtUtils::CBuilder*,ExtUtils::Command.*,ExtUtils::Install.3*}
%exclude %{_mandir}/man3/{ExtUtils::Installed.3*,ExtUtils::Packlist.3*,ExtUtils::Manifest.3*}
%exclude %{_mandir}/man3/{ExtUtils::Command::MM*,ExtUtils::Liblist.3*,ExtUtils::MM.3*,ExtUtils::MM_*}
%exclude %{_mandir}/man3/{ExtUtils::MY.3*,ExtUtils::MakeMaker*,ExtUtils::Mkbootstrap.3*,IPC::Semaphore.*}
%exclude %{_mandir}/man3/{ExtUtils::Mksymlists.3*,ExtUtils::testlib.3*,ExtUtils::MM::Utils.*,IPC::SharedMem.*}
%exclude %{_mandir}/man3/{ExtUtils::ParseXS*,ExtUtils::Typemaps*,File::Fetch.3*,File::Path.3*,IPC::SysV.*}
%exclude %{_mandir}/man3/{File::Temp.3*,Filter::Util::*,Filter::Simple.3*,Getopt::Long.3*,IPC::Msg.*}
%exclude %{_mandir}/man3/{IO::Compress::*,Compress::Zlib*,File::GlobMapper.*,IO::Uncompress::*}
%exclude %{_mandir}/man3/{IO::Socket::IP.*,HTTP::Tiny*,IPC::Cmd.3*,JSON::PP*,Net::Cmd.*,Net::Config.*}
%exclude %{_mandir}/man3/{Net::Domain.*,Net::FTP.*,Net::libnetFAQ.*,Net::NNTP.*,Net::Netrc.*,Net::POP3.*}
%exclude %{_mandir}/man3/{Net::SMTP.*,Net::Time.*,Locale::Codes::*,Locale::Codes.*,Locale::Country.*}
%exclude %{_mandir}/man3/{Locale::Currency.*,Locale::Language.*,Locale::Script.*,Locale::Maketext.*}
%exclude %{_mandir}/man3/{Locale::Maketext::Cookbook.*,Locale::Maketext::Guts.*,Locale::Maketext::GutsLoader.*}
%exclude %{_mandir}/man3/{Locale::Maketext::TPJ13.*,Math::BigFloat.*,Math::BigInt*,Math::BigRat.*,MIME::*,Cwd*}
%exclude %{_mandir}/man3/{Module::CoreList*,Module::Load.*,Module::Load::Conditional*,Module::Metadata.3pm*}
%exclude %{_mandir}/man3/{File::Spec*,Params::Check*,PerlIO::via::QuotedPrint.*,Perl::OSType.3pm*,parent.3*}
%exclude %{_mandir}/man3/{Pod::Checker.*,Pod::Escapes.*,Pod::PlainText.*,Pod::Select.*,Pod::Perldoc*,Pod::Usage.*}
%exclude %{_mandir}/man3/{Pod::Man*,Pod::ParseLink*,Pod::Text*,Pod::Simple*,List::Util*,Scalar::Util*,Sub::Util*}
%exclude %{_mandir}/man3/{Storable.*,Sys::Syslog.*,Term::ANSIColor*,Term::Cap.*,App::Prove*,TAP*,Test::Harness*}
%exclude %{_mandir}/man3/{ok*,Test::More*,Test::Builder*,Test::Tester*,Test::Simple*,Test::Tutorial*,Test::use::*}
%exclude %{_mandir}/man3/{Test2*,Text::Balanced.*,Text::ParseWords.*,Text::Tabs.*,Text::Wrap.*,Thread::Queue.*}
%exclude %{_mandir}/man3/{Time::HiRes.*,Time::Local.*,Socket.3*,threads.3*,threads::shared*,Unicode::Collate.*}
%exclude %{_mandir}/man3/{Unicode::Collate::*,Unicode::Normalize.*,version.3*,version::Internals.3*,Devel::PPPort*}

%doc README Changes
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Mar 4 2021 tianwei <tianwei12@huawei.com> - 4:5.32.0-3
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:perl build error

* Mon Aug 17 2020 openEuler Buildteam <buildteam@openeuler.org> - 4:5.32.0-2
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:delete the temporary unneeded behavior for upgrade of perl

* Thu Aug 13 2020 openEuler Buildteam <buildteam@openeuler.org> - 4:5.32.0-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:bump version to 5.32.0

* Sat Mar 21 2020 openEuler Buildteam <buildteam@openeuler.org> - 4:5.28.0-434
- Type:NA
- ID:NA
- SUG:NA
- DESC:add build requires of gdb

* Tue Feb 11 2020 openEuler Buildteam <buildteam@openeuler.org> - 4:5.28.0-433
- Type:NA
- ID:NA
- SUG:NA
- DESC:add subpackage perl-libs

* Mon Jan 13 2020 openEuler Buildteam <buildteam@openeuler.org> - 4:5.28.0-432
- Type:NA
- ID:NA
- SUG:NA
- DESC:delete unneeded source in perl

* Sat Jan 11 2020 openEuler Buildteam <buildteam@openeuler.org> - 4:5.28.0-431
- Type:NA
- ID:NA
- SUG:NA
- DESC:add macros that used for perl

* Fri Jan 2 2020 openEuler Buildteam <buildteam@openeuler.org> - 4:5.28.0-430
- Type:NA
- ID:NA
- SUG:NA
- DESC:delete unneeded patch

* Mon Dec 23 2019 openEuler Buildteam <buildteam@openeuler.org> - 4:5.28.0-429
- Type:NA
- ID:NA
- SUG:NA
- DESC:change info in comments and changelog

* Tue Oct 29 2019 shenyangyang<shenyangyang4@huawei.com> - 4:5.28.0-428
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:add build requires of bzip2-devel and gdbm-devel to solve build problem

* Wed Sep 18 2019 shenyangyang<shenyangyang4@huawei.com> - 4:5.28.0-427
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:revise spec

* Tue Aug 20 2019 wangchong<wangchong56@huawei.com> - 4:5.28.0-426
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: rename patches

* Thu Apr 11 2019 zhangzhihui<zhangzhihui23@huawei.com> - 4:5.28.0-425
- Type:cves
- ID: fix CVE-2018-18312
- SUG:restart
- DESC:fix cves

* Tue Mar 5 2019 wangjia <wangjia55@huawei.com> - 4:5.28.0-424
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:disable perl-ExtUtils-CBuilder and perl-CPAN require

* Mon Sep 24 2018 openEuler Buildteam <buildteam@openeuler.org> - 4:5.28.0-423
- Package Init
