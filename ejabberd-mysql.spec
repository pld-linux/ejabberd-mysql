
%define		_snap	20070926r390

Summary:	Ejabberds native MySQL drivers
Summary(pl.UTF-8):	Natywne sterowniki do MySQL dla ejabberda
Name:		ejabberd-mysql
Version:	0
Release:	0.%{_snap}.1
License:	GPL
Group:		Applications/Communications
# get it from https://svn.process-one.net/ejabberd-modules/mysql/trunk/src/ and drop onto distfiles
Source0:	%{name}.tar.gz
# Source0-md5:	3f3b5c59ebb5a807ec2d6c5ec31e795b
URL:		http://ejabberd.jabber.ru/
BuildRequires:	erlang >= R9C
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	ejabberd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ejabberds native MySQL drivers.

%description -l pl.UTF-8
Natywne sterowniki do MySQL dla ejabberda.

%prep
%setup -q -n %{name}

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
