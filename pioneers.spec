Summary: 	Playable implementation of the Settlers of Catan 
Name: 		pioneers
Version: 	14.1
Release:        3
Group: 		Games/Boards
License: 	GPLv2+
Url: 		http://pio.sourceforge.net/
Source: 	http://downloads.sourceforge.net/project/pio/Source/%{name}-%{version}.tar.gz
Source2:	pioneers-0.9.55-icons.tar.bz2
Patch: pioneers-0.12.1-desktopentry.patch
BuildRequires:  pkgconfig(libgnome-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
%if %mdvver >= 201200
BuildRequires:  pkgconfig(libnotify) >= 0.7.4
%endif
BuildRequires:  avahi-client-devel
BuildRequires:  scrollkeeper
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
Provides: gnocatan
Obsoletes: gnocatan

%description 
Pioneers is an Internet playable implementation of the Settlers of
Catan board game.  The aim is to remain as faithful to the board game
as is possible.

%package 	server-console
Summary:	Pioneers Console Server
Group: 		Games/Boards
Requires:	pioneers-server-data = %version
Provides: gnocatan-server-console
Obsoletes: gnocatan-server-console
%description 	server-console
Pioneers is an Internet playable implementation of the Settlers of
Catan board game.  The aim is to remain as faithful to the board game
as is possible.
The meta server registers available game servers and offers them to new
players. It can also create new servers on client request.


%package 	server-gtk
Summary:	Pioneers GTK Server
Group: 		Games/Boards
Requires:	pioneers-server-data = %version
Provides: gnocatan-server-gtk
Obsoletes: gnocatan-server-gtk
%description 	server-gtk
Pioneers is an Internet playable implementation of the Settlers of
Catan board game.  The aim is to remain as faithful to the board game
as is possible.

The server has a user interface in which you can customise the game
parameters.  Customisation is fairly limited at the moment, but this
should change in later versions.  Once you are happy with the game
parameters, press the Start Server button, and the server will start
listening for client connections.

%package 	server-data
Summary: 	Pioneers Data
Group: 		Games/Boards
Provides: gnocatan-server-data
Obsoletes: gnocatan-server-data
%description 	server-data
Pioneers is an Internet playable implementation of the Settlers of
Catan board game.  The aim is to remain as faithful to the board game
as is possible.

This package contains the data files for a game server, including a
computer player that can take part in Pioneers games.


%prep
%setup -q -a 2
%apply_patches


%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name --with-gnome
desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Boards" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

cp -r icons %buildroot%_datadir/

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%update_scrollkeeper
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%clean_menus
%endif

%if %mdkversion < 200900
%post server-gtk
%update_menus
%endif

%if %mdkversion < 200900
%postun server-gtk
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/pioneers
%{_bindir}/pioneers-editor
%{_datadir}/applications/pioneers.desktop
%{_datadir}/applications/pioneers-editor.desktop
%{_datadir}/pixmaps/pioneers.png
%{_datadir}/pixmaps/pioneers-editor.png
%{_datadir}/pixmaps/pioneers/
%dir %{_datadir}/games/pioneers
%{_datadir}/games/pioneers/themes/
%{_mandir}/man6/pioneers.6*
%{_mandir}/man6/pioneers-editor.6*
%if %mdvver <= 201100
%_datadir/omf/pioneers
%endif
%_datadir/icons/hicolor/*/apps/pioneers.*
%_datadir/icons/hicolor/*/apps/pioneers-editor.*
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name-editor.png
%_liconsdir/%name-editor.png
%_miconsdir/%name-editor.png

%files server-console
%defattr(-,root,root)
%doc README
%{_bindir}/pioneers-server-console
%{_bindir}/pioneers-meta-server
%{_mandir}/man6/pioneers-server-console.6*
%{_mandir}/man6/pioneers-meta-server.6*

%files server-gtk
%defattr(-,root,root)
%doc README
%{_bindir}/pioneers-server-gtk
%{_datadir}/applications/pioneers-server.desktop
%{_mandir}/man6/pioneers-server-gtk.6*
%_datadir/pixmaps/%name-server.png
%_datadir/icons/hicolor/*/apps/pioneers-server.*
%_iconsdir/%name-server.png
%_liconsdir/%name-server.png
%_miconsdir/%name-server.png

%files server-data
%defattr(-,root,root)
%doc README
%{_bindir}/pioneersai
%{_mandir}/man6/pioneersai.6*
%dir %{_datadir}/games/pioneers
%{_datadir}/games/pioneers/computer_names
%{_datadir}/games/pioneers/*.game


%changelog
* Tue May 29 2012 Götz Waschk <waschk@mandriva.org> 14.1-1mdv2011.0
+ Revision: 801062
- fix file list again for backports

* Tue May 29 2012 Götz Waschk <waschk@mandriva.org> 14.1-1
+ Revision: 801050
- update file list for rpm5
- update to new version 14.1

* Mon Oct 31 2011 Götz Waschk <waschk@mandriva.org> 0.12.5-1
+ Revision: 707985
- new version
- enable avahi support
- enable notification support on Cooker

* Tue Aug 30 2011 Götz Waschk <waschk@mandriva.org> 0.12.4-1
+ Revision: 697438
- drop patch 1
- update to new version 0.12.4

* Tue Oct 05 2010 Götz Waschk <waschk@mandriva.org> 0.12.3.1-1mdv2011.0
+ Revision: 583063
- update to new version 0.12.3.1

* Mon Jan 25 2010 Götz Waschk <waschk@mandriva.org> 0.12.3-1mdv2010.1
+ Revision: 496252
- update build deps
- new version
- rediff patch 1
- update file list

* Sun Aug 09 2009 Götz Waschk <waschk@mandriva.org> 0.12.2-3mdv2010.0
+ Revision: 412352
- update license
- fix format strings

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.12.2-2mdv2009.0
+ Revision: 268999
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - use %%update_scrollkeeper/%%clean_scrollkeeper

* Sun May 04 2008 Götz Waschk <waschk@mandriva.org> 0.12.2-1mdv2009.0
+ Revision: 201025
- new version
- new version
- update the patch

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Oct 07 2007 Götz Waschk <waschk@mandriva.org> 0.11.3-1mdv2008.1
+ Revision: 95679
- new version
- add gpg signature to the sources
- fix desktop entries

* Sun Aug 05 2007 Götz Waschk <waschk@mandriva.org> 0.11.2-1mdv2008.0
+ Revision: 59105
- new version

* Sun Jul 22 2007 Götz Waschk <waschk@mandriva.org> 0.11.1-1mdv2008.0
+ Revision: 54471
- Import pioneers



* Sun Jul 22 2007 Götz Waschk <waschk@mandriva.org> 0.11.1-1mdv2008.0
- New version 0.11.1

* Sun Sep 17 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdv2007.0
- New version 0.10.2

* Sun Aug 27 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdv2007.0
- New release 0.10.1

* Fri Aug  4 2006 G�tz Waschk <waschk@mandriva.org> 0.9.64-3mdv2007.0
- fix old menu

* Tue Jun 20 2006 G�tz Waschk <waschk@mandriva.org> 0.9.64-2mdv2007.0
- xdg menu

* Tue Jun 06 2006 Götz Waschk <waschk@mandriva.org> 0.9.64-1
- New release 0.9.64

* Tue May 30 2006 Götz Waschk <waschk@mandriva.org> 0.9.63-1
- New release 0.9.63

* Sun May 28 2006 Götz Waschk <waschk@mandriva.org> 0.9.62-1mdk
- New release 0.9.62

* Sun Apr 09 2006 Götz Waschk <waschk@mandriva.org> 0.9.61-1mdk
- New release 0.9.61

* Thu Mar  9 2006 G�tz Waschk <waschk@mandriva.org> 0.9.55-2mdk
- don't use rsvg anymore for the icons to allow backports

* Thu Feb 09 2006 Götz Waschk <waschk@mandriva.org> 0.9.55-1mdk
- New release 0.9.55

* Tue Feb 07 2006 Götz Waschk <waschk@mandriva.org> 0.9.54-1mdk
- New release 0.9.54

* Wed Jan 25 2006 G�tz Waschk <waschk@mandriva.org> 0.9.49-1mdk
- use rsvg for the icons
- New release 0.9.49

* Sat Dec 31 2005 G�tz Waschk <waschk@mandriva.org> 0.9.40-4mdk
- fix icon transparency

* Sat Dec 31 2005 G�tz Waschk <waschk@mandriva.org> 0.9.40-3mdk
- use the svg icon

* Tue Dec 27 2005 G�tz Waschk <waschk@mandriva.org> 0.9.40-2mdk
- fix obsoletes

* Wed Dec 21 2005 G�tz Waschk <waschk@mandriva.org> 0.9.40-1mdk
- fix menu
- New release 0.9.40
- use mkrel

* Sun Nov 20 2005 Götz Waschk <waschk@mandriva.org> 0.9.33-2mdk
- rebuild for new openssl

* Thu Nov 03 2005 Götz Waschk <waschk@mandriva.org> 0.9.33-1mdk
- New release 0.9.33

* Thu Sep 01 2005 Götz Waschk <waschk@mandriva.org> 0.9.23-2mdk
- rebuild to remove glitz dep

* Mon Aug 22 2005 Götz Waschk <waschk@mandriva.org> 0.9.23-1mdk
- New release 0.9.23

* Fri Jul 15 2005 Götz Waschk <waschk@mandriva.org> 0.9.19-1mdk
- add the editor
- fix buildrequires
- new version
- renamed from gnocatan

* Sat Mar 26 2005 Götz Waschk <waschk@linux-mandrake.com> 0.8.1.59-1mdk
- New release 0.8.1.59

* Thu Mar 03 2005 Götz Waschk <waschk@linux-mandrake.com> 0.8.1.54-1mdk
- New release 0.8.1.54

* Sat Feb  5 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.8.1.53-1mdk
- New release 0.5.1.53

* Fri Feb  4 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.52-1mdk
- New release 0.8.1.52

* Wed Jan 26 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.51-1mdk
- New release 0.8.1.51

* Sun Jan 23 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.50-1mdk
- New release 0.8.1.50

* Sun Jan  9 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.48-1mdk
- New release 0.8.1.48

* Sat Dec  4 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.45-1mdk
- New release 0.8.1.45

* Sun Nov 21 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.43-1mdk
- New release 0.8.1.43

* Sat Nov 13 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.42-1mdk
- New release 0.8.1.42

* Sun Oct 24 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.40-1mdk
- New release 0.8.1.40

* Sun Oct 17 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.39-1mdk
- New release 0.8.1.39

* Sat Oct  9 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.38-1mdk
- New release 0.8.1.38

* Fri Oct  1 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.37-1mdk
- New release 0.8.1.37

* Mon Sep 27 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1.36-1mdk
- New release 0.8.1.36

* Fri Jul  9 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.8.1.30-1mdk
- drop yelp pregeneration call
- fix source URL
- New release 0.8.1.30

* Sat Feb  7 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.8.1.16-2mdk
- fix directory ownership

* Tue Jan 27 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.8.1.16-1mdk
- new version

* Mon Oct 20 2003 G�tz Waschk <waschk@linux-mandrake.com> 0.8.0.0-1mdk
- initial package


* Sun May 19 2002 Roman Hodek <roman@hodek.net>
- 0.6.99 as beta for 0.7.0

* Sun Aug 27 2000 Steve Langasek <vorlon@dodds.net>
- 0.6.1 released

* Tue Jun 20 2000 Steve Langasek <vorlon@dodds.net>
- updated version number

* Thu Jun 01 2000 Steve Langasek <vorlon@dodds.net>
- Updated to behave more like the filesystem standard tells us to (and
  more like configure expects us to)

* Sun May 07 2000 Dave Cole <adve@dccs.com.au>
- Removed ship building development card

* Mon May 01 2000 Andy Heroff <aheroff@mediaone.net>
- SourceForge release version 0.5.0

* Fri Sep 03 1999 Dave Cole <dave@dccs.com.au>
- Modifications to build 0.4.0

* Sun May 23 1999 Preben Randhol <randhol@pvv.org>
- Building version 0.31

* Wed May 12 1999 Preben Randhol <randhol@pvv.org>
- First try at making the packages
