#
# Conditional build:
%bcond_with	logdb	# server-side message logging support for mysql5 driver
#
%define		_snap	20070926r390

%define	realname	ejabberd-mysql

Summary:	Ejabberd's native MySQL drivers
Summary(pl.UTF-8):	Natywne sterowniki do MySQL-a dla demona ejabberd
Name:		%{realname}
Version:	0
Release:	1.%{_snap}.1
License:	GPL
Group:		Applications/Communications
# get it from https://svn.process-one.net/ejabberd-modules/mysql/trunk/src/ and drop onto distfiles
Source0:	%{realname}.tar.gz
# Source0-md5:	3f3b5c59ebb5a807ec2d6c5ec31e795b
Patch0:		%{realname}-logdb_mysql5.patch
URL:		http://ejabberd.jabber.ru/
BuildRequires:	erlang >= R9C
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	ejabberd-logdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ejabberds native MySQL drivers.

%description -l pl.UTF-8
Natywne sterowniki do MySQL-a dla demona ejabberd.

%prep
%setup -q -n %{realname}
%if %{with logdb}
%patch0 -p0
%endif

%build
erlc mysql*.erl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ejabberd/ebin

install *.beam $RPM_BUILD_ROOT%{_libdir}/ejabberd/ebin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/ejabberd/ebin/mysql*.beam
