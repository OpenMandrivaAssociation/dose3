%define name	dose3
%define version 2.9.15
%define release	1

%if %mdkversion > 200900
%define camlzip_inc +camlzip
%else
%define camlzip_inc +site-lib/camlzip
%endif

Summary:	A tool to check consistency of rpm repositories
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		System/Configuration/Packaging
# No website yet
URL:		http://gforge.info.ucl.ac.be/frs/?group_id=35
Source:		%name-%version.tar.gz
BuildRequires:	ocaml ocaml-findlib ocaml-extlib ocaml-pcre ocaml-sqlite ocaml-xml-light ocaml-ounit ocaml-ocamlgraph-devel
Buildrequires:  camlp4 rpm-devel cudf-ocaml-devel
BuildRequires:	ocaml-camlzip-devel curl-devel ocaml-lzma ocaml-expat ocaml-sqlite-devel ocaml-xml-light-devel
BuildRequires:	ocaml-json-wheel-devel ocaml-json-static ocaml-ocamlnet ocaml-ocamlnet-devel
Buildrequires:	ocaml-extlib-devel ocaml-expat-devel ocaml-ocamlgraph-devel ocaml-curl-devel
Buildroot:	%_tmppath/%name-%version

%description
Dose3 is a tool to check consistency of Mandriva Linux rpm repositories
(that is, of hdlist files.)

%prep
%setup -q -n %name-%version

%build
./configure --with-rpm5 \
	--with-xml \
	--with-zip \
	--with-oUnit \
	--with-curl \
	--with-ocamlgraph 
#	--with-sqlite \
#	--with-postgresql \

make

%install
%__rm -rf %buildroot
%makeinstall_std

%clean
%__rm -rf %buildroot

%files
%doc COPYING INSTALL
%_bindir/*
%_libdir/%name




%changelog
* Mon Apr 11 2011 Antoine Ginies <aginies@mandriva.com> 2.9.2-2
- add curl, ocamlgraph options
- add rpm5 support

* Fri Apr 8 2011 Antoine Ginies <aginies@mandriva.com> 2.9.2
- first release
