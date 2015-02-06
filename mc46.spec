%define		oname	mc

Name:		mc46
Version:	4.6.3
Release:	3
Summary:	So called russian fork of Midnight Commander
License:	GPLv2
Group:		File tools
URL:		http://mc.redhat-club.org
Source0:	%{oname}-%{version}.tar.bz2
BuildRequires:	pkgconfig(glib-2.0)
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
%makeinstall_std
%__cp %{buildroot}%{_datadir}/%{oname}/bin/* %{buildroot}%{_libdir}/%{oname}/

%find_lang %{oname} --with-man

%files -f %{oname}.lang
%doc COPYING README INSTALL AUTHORS
%{_bindir}/*
%{_libdir}/%{oname}
%{_sysconfdir}/%{oname}
%{_mandir}/man1/*
%{_datadir}/%{oname}



%changelog
* Thu Feb 16 2012 Andrey Bondrov <abondrov@mandriva.org> 4.6.3-1mdv2011.0
+ Revision: 775257
- imported package mc46


* Sat Nov 07 2009 Andrey Bondrov <bondrov@math.dvgu.ru> 4.6.3-1mib2010.0
- Build for 2010.0
- Added glib2-devel, gpm-devel and libx11-devel to BuildRequires
- Added configure options
- MIB (Mandriva Italia Backports)  - http://mib.pianetalinux.org/

* Thu Dec 16 2008 Andrey Bondrov <bondrov@math.dvgu.ru> 4.6.3-1mib2008.1
- 4.6.3 Final
- MIB (Mandriva Italia Backports)  - http://mib.pianetalinux.org/

* Thu Nov 28 2008 Andrey Bondrov <bondrov@math.dvgu.ru> 4.6.3-svn92.1mib2008.1
- SVN revision 92.
- New features added (Shift+F1/F2, Alt+. and Alt+.)
- MIB (Mandriva Italia Backports)  - http://mib.pianetalinux.org/

* Thu Nov 26 2008 Andrey Bondrov <bondrov@math.dvgu.ru> 4.6.2-svn47.1mib2008.1
- First MIB build
- MIB (Mandriva Italia Backports)  - http://mib.pianetalinux.org/
