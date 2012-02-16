%define		oname	mc

Name:		mc46
Version:	4.6.3
Release:	%mkrel 1
Summary:	So called russian fork of Midnight Commander
License:	GPLv2
Group:		File tools
URL:		http://mc.redhat-club.org
Source0:	%{oname}-%{version}.tar.bz2
BuildRequires:	glib2-devel
BuildRequires:	gpm-devel
BuildRequires:	X11-devel
BuildRequires:	bison
Conflicts:	%{oname}

%description
So called russian fork of Midnight Commander.
It has better default syntax highlighting for spec files and some
other useful features that we don't have in 4.7+.

Midnight Commander is a visual shell much like a file manager,
only with way more features. It is text mode, but also includes
mouse support if you are running GPM.  Its coolest feature is
the ability to ftp, view tar, zip files, and poke into RPMs for
specific files. This is "revived" version with many patches applied.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure --with-gpm-mouse --with-x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
%__cp %{buildroot}%{_datadir}/%{oname}/bin/* %{buildroot}%{_libdir}/%{oname}/

%find_lang %{oname} --with-man

%clean
%__rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc COPYING README INSTALL AUTHORS
%{_bindir}/*
%{_libdir}/%{oname}
%{_sysconfdir}/%{oname}
%{_mandir}/man1/*
%{_datadir}/%{oname}

