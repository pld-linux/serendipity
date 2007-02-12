Summary:	Personal publishing system
Summary(pl.UTF-8):	Osobisty system publikacji
Name:		serendipity
Version:	1.1
Release:	1
License:	BSD
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/php-blog/%{name}-%{version}.tar.bz2
# Source0-md5:	6b743609dde3557c22424dfda3176ce5
Source1:	%{name}.conf
URL:		http://www.s9y.org/
Requires:	%{name}(DB_driver)
Requires:	%{name}-event_browsercompatibility = %{version}-%{release}
Requires:	%{name}-event_emoticate = %{version}-%{release}
Requires:	%{name}-event_nl2br = %{version}-%{release}
Requires:	%{name}-event_spamblock = %{version}-%{release}
Requires:	%{name}-event_s9ymarkup = %{version}-%{release}
Requires:	ImageMagick
Requires:	php(gd)
Requires:	php(gettext)
Requires:	php(iconv)
Requires:	php(mbstring)
Requires:	php(openssl)
Requires:	php(pcre)
Requires:	php(xml)
Requires:	php(xmlrpc)
Requires:	php(zlib)
Requires:	webapps
Requires:	webserver(php) >= 4.3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}
%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}

%description
%description -l pl.UTF-8

%package db-pgsql
Summary:	Serendipity DB Driver for PostgreSQL
Summary(pl.UTF-8):	Sterownik bazy danych PostreSQL dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	php(pgsql)
Provides:	%{name}(DB_driver) = %{version}-%{release}

%description db-pgsql
This virtual package provides PostgreSQL database backend for
Serendipity.

%description db-pgsql -l pl.UTF-8
Ten wirtualny pakiet dostarcza backend bazy danych PostgreSQL dla
Serendipity.

%package db-mysql
Summary:	Serendipity DB Driver for MySQL
Summary(pl.UTF-8):	Sterownik bazy danych MySQL dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	php(mysql)
Provides:	%{name}(DB_driver) = %{version}-%{release}

%description db-mysql
This virtual package provides MySQL database backend for Serendipity.

%description db-mysql -l pl.UTF-8
Ten wirtualny pakiet dostarcza backend bazy danych MySQL dla
Serendipity.

%package db-sqlite3
Summary:	Serendipity DB Driver for SQLite3
Summary(pl.UTF-8):	Sterownik bazy danych SQLite3 dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	php(sqlite3)
Provides:	%{name}(DB_driver) = %{version}-%{release}

%description db-sqlite3
This virtual package provides SQLite3 database backend for
Serendipity.

%description db-sqlite3 -l pl.UTF-8
Ten wirtualny pakiet dostarcza backend bazy danych SQLite3 dla
Serendipity.

%package event_bbcode
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_bbcode
BBcode hooks for Serendipity editor.

%description event_bbcode -l pl.UTF-8
Rozszerzenia BBCode dla edytora Serendipity.

%package event_browsercompatibility
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

# FIXME
%description event_browsercompatibility
Event extension for Serendipity.

%description event_browsercompatibility -l pl.UTF-8
Rozszerzenie obsługi zdarzeń dla Serendipity.

%package event_contentrewrite
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_contentrewrite
Extension for Serendipity editor that enables rewriting user defined
frazes

%description event_contentrewrite -l pl.UTF-8
Rozszerzenie dla edytora Serendipity pozwalające na podmienianie
zdefiniowanych przez użytkownia słów kluczowych

%package event_creativecommons
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugin_creativecommons = %{version}-%{release}

%description event_creativecommons
Extension that that displays on sidebar user choosed Creatice Common
license.

%description event_creativecommons -l pl.UTF-8
Rozszerzenie wyświetlające na panelu wybraną przez użytkownika
licencję Creative Commons.

%package event_emoticate
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_emoticate
Extension for Serendipity editor that converts smilies to icons.

%description event_emoticate -l pl.UTF-8
Rozszerzenie dla edytora Serendipity zamieniające emotikony tekstowe
na ikony.

%package event_entryproperties
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

# FIXME
%description event_entryproperties
Event extension for Serendipity.

%description event_entryproperties -l pl.UTF-8
Rozszerzenie obsługi zdarzeń dla Serendipity.

%package event_karma
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

# FIXME
%description event_karma
Event extension for Serendipity.

%description event_karma -l pl.UTF-8
Rozszerzenie obsługi zdarzeń dla Serendipity.

%package event_livesearch
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

# FIXME
%description event_livesearch
Event extension for Serendipity.

%description event_livesearch -l pl.UTF-8
Rozszerzenie obsługi zdarzeń dla Serendipity.

%package event_mailer
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_mailer
Extension allowing to send article to user defined email.

%description event_mailer -l pl.UTF-8
Rozszerzenie pozwalące wysłać artykuł na wskazany adres e-mail.

%package event_nl2br
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_nl2br
Extension for Serendipity editor converting any newline from entry
creation into HTML break.

%description event_nl2br -l pl.UTF-8
Rozszerzenie edytora Serendipity zmieniające wystąpienia nowych linii
w modyfikowanym tekście na odpowiedni znacznik HTML.

%package event_s9ymarkup
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_s9ymarkup
Native extension for Serendipity editor.

%description event_s9ymarkup -l pl.UTF-8
Natywne rozszerzenie dla edytora Serendipity.

%package event_searchhighlight
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie osbługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

# FIXME
%description event_searchhighlight
Event extension for Serendipity.

%description event_searchhighlight -l pl.UTF-8
Rozszerzenie osbługi zdarzeń dla Serendipity.

%package event_spamblock
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

# FIXME
%description event_spamblock
Event extension for Serendipity.

%description event_spamblock -l pl.UTF-8
Rozszerzenie obsługi zdarzeń dla Serendipity.

%package event_spartacus
Summary:	Sidebar plugin manager for Serendipity
Summary(pl.UTF-8):	Zarządca wtyczek dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_spartacus
Sidebar plugin manager for Serendipity that allows installing plugins
from Serendipity repository.

%description event_spartacus -l pl.UTF-8
Rozszerzenie pozwalające na instalację dodatkowych wtyczek z
repozytorium Serendipity.

%package event_statistics
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_statistics
Extension adding link to internal Serendipity statistics.

%description event_statistics -l pl.UTF-8
Rozszerzenie dodające odnośnik do wewnętrznych statystyk Serendipity.

%package event_templatechooser
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugin_templatechooser = %{version}-%{release}

# FIXME
%description event_templatechooser
Event extension for Serendipity.

%description event_templatechooser -l pl.UTF-8
Rozszerzenie obsługi zdarzeń dla Serendipity.

%package event_textile
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_textile
Textile hooks for Serendipity editor.

%description event_textile -l pl.UTF-8
Rozszerzenia Textile dla edytora Serendipity.

%package event_textwiki
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_textwiki
Textwiki hooks for Serendipity editor.

%description event_textwiki -l pl.UTF-8
Rozszerzenia Textwiki dla edytora Serendipity.

%package event_trackexits
Summary:	Event extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie obsługi zdarzeń dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description event_trackexits
Extension encondig URLs in articles that giving statistics about
wayouts from blog.

%description event_trackexits -l pl.UTF-8
Rozszerzenie zmieniające kod odnośników w artykułach zbierające dane
na temat kliknięć (wyjść z blogu).

%package event_weblogping
Summary:	Editor extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie edytora dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

# FIXME
%description event_weblogping
Editor extension for Serendipity.

%description event_weblogping -l pl.UTF-8
Rozszerzenie edytora dla Serendipity.

%package event_xhtmlcleanup
Summary:	Editor extension for Serendipity
Summary(pl.UTF-8):	Rozszerzenie edytora dla Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

# FIXME
%description event_xhtmlcleanup
Editor extension for Serendipity.

%description event_xhtmlcleanup -l pl.UTF-8
Rozszerzenie edytora dla Serendipity.

%package plugin_comments
Summary:	Sidebar plugin for Serendipity
Summary(pl.UTF-8):	Wtyczka dla paneli Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description plugin_comments
Displays a list of recently submitted comments.

%description plugin_comments -l pl.UTF-8
Wtyczka wyświetlająca listę ostatnio dodanych komentarzy.

%package plugin_creativecommons
Summary:	Sidebar plugin for Serendipity
Summary(pl.UTF-8):	Wtyczka dla paneli Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-event_creativecommons = %{version}-%{release}

%description plugin_creativecommons
Displays chosen Creative Commons license data

%description plugin_creativecommons -l pl.UTF-8
Wyświetla wybraną licencję Creative Commons

%package plugin_entrylinks
Summary:	Sidebar plugin for Serendipity
Summary(pl.UTF-8):	Wtyczka dla paneli Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

# FIXME
%description plugin_entrylinks
Sidebar plugin for Serendipity.

%description plugin_entrylinks -l pl.UTF-8
Wtyczka dla paneli Serendipity.

%package plugin_eventwrapper
Summary:	Sidebar plugin for Serendipity
Summary(pl.UTF-8):	Wtyczka dla paneli Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description plugin_eventwrapper
Plugin allowing using event extensions in sidebar.

%description plugin_eventwrapper -l pl.UTF-8
Wtyczka pozwalająca używać rozszerzeń (event_) wewnątrz paneli.

%package plugin_history
Summary:	Sidebar plugin for Serendipity
Summary(pl.UTF-8):	Wtyczka dla paneli Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

# FIXME
%description plugin_history
Sidebar plugin for Serendipity.

%description plugin_history -l pl.UTF-8
Wtyczka dla paneli Serendipity.

%package plugin_recententries
Summary:	Sidebar plugin for Serendipity
Summary(pl.UTF-8):	Wtyczka dla paneli Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description plugin_recententries
Shows a quick list of recently made entries.

%description plugin_recententries -l pl.UTF-8
Wtyczka pokazująca krótką listą ostatnio dodanych wpisów.

%package plugin_remoterss
Summary:	Sidebar plugin for Serendipity
Summary(pl.UTF-8):	Wtyczka dla paneli Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description plugin_remoterss
Plugin that enables to display foreign RSS feed embedded into blog.

%description plugin_remoterss -l pl.UTF-8
Wtyczka pozwalająca na wyświetlanie za pomocą RSS treści innych
blogów.

%package plugin_shoutbox
Summary:	Sidebar plugin for Serendipity
Summary(pl.UTF-8):	Wtyczka dla paneli Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description plugin_shoutbox
Shows a simple form area where users can enter any comments they want.
Those comments are displayed immediately on sidebar.

%description plugin_shoutbox -l pl.UTF-8
Wtyczka wyświetlająca prosty formularz, przez który użytkownicy mogą
dodawać komentarze wyświetlane natychmiast na panelu.

%package plugin_templatedropdown
Summary:	Sidebar plugin for Serendipity
Summary(pl.UTF-8):	Wtyczka dla paneli Serendipity
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-event_templatedropdown = %{version}-%{release}

%description plugin_templatedropdown
Shows on sidebar availaible themes, which could be chosen by any
visitor to change the layout displayed to him.

%description plugin_templatedropdown -l pl.UTF-8
Wtyczka wyświetlająca na panelu dostępne motywy, którymi użytkownicy
mogą dostosywywać wyświetlanie wg swoich preferencji.

%prep
%setup -q -n %{name}
rm -f docs/LICENSE
rm -rf templates_c uploads

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_appdir},%{_sysconfdir}}
install -d $RPM_BUILD_ROOT/var/lib/%{name}/{archives,templates_c,uploads}

ln -s /var/lib/%{name}/uploads $RPM_BUILD_ROOT%{_appdir}/uploads
ln -s /var/lib/%{name}/archives $RPM_BUILD_ROOT%{_appdir}/archives
ln -s /var/lib/%{name}/templates_c $RPM_BUILD_ROOT%{_appdir}/templates_c

cp -R * $RPM_BUILD_ROOT%{_appdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf

touch $RPM_BUILD_ROOT%{_appdir}/.htaccess
touch $RPM_BUILD_ROOT%{_appdir}/serendipity_config_local.inc.php

ln -s %{_appdir}/serendipity_config_local.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner -e %{name} <<-EOF
To finish your configuration DO NOT FORGET to:

1) Create some SQL database owned by some user
2) Run a browser and visit: http://`hostname`/serendipity/index.php
EOF

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%files
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%{_sysconfdir}/%{name}.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf

%dir %{_appdir}/
%dir %{_appdir}/sql
%dir %{_appdir}/plugins
%dir /var/lib/%{name}
%dir %attr(770,root,http) /var/lib/%{name}/*

%{_appdir}/bundled-libs
%{_appdir}/deployment
%{_appdir}/docs
%{_appdir}/htmlarea
%{_appdir}/include
%{_appdir}/lang
%{_appdir}/templates

%{_appdir}/archives
%{_appdir}/templates_c
%{_appdir}/uploads

%{_appdir}/comment.php
%{_appdir}/exit.php
%{_appdir}/index.php
%{_appdir}/rss.php
%{_appdir}/serendipity.css.php
%{_appdir}/serendipity_admin.php
%{_appdir}/serendipity_admin_image_selector.php
%{_appdir}/serendipity_config.inc.php
%{_appdir}/serendipity_define.js.php
%{_appdir}/serendipity_editor.js
%{_appdir}/serendipity_xmlrpc.php
%{_appdir}/sql/db.sql
%{_appdir}/wfwcomment.php
%exclude %{_appdir}/include/db/mysql.inc.php
%exclude %{_appdir}/include/db/mysqli.inc.php
%exclude %{_appdir}/include/db/postgres.inc.php
%exclude %{_appdir}/include/db/sqlite.inc.php
%attr(660,root,http) %config(noreplace) %verify(not md5 mtime size) %{_appdir}/.htaccess
%attr(660,root,http) %config(noreplace) %verify(not md5 mtime size) %{_appdir}/serendipity_config_local.inc.php

%files db-pgsql
%defattr(644,root,root,755)
%{_appdir}/sql/*postgres*
%{_appdir}/include/db/*postgres*

%files db-mysql
%defattr(644,root,root,755)
%{_appdir}/sql/*mysql*
%{_appdir}/include/db/*mysql*

%files db-sqlite3
%defattr(644,root,root,755)
%{_appdir}/sql/*sqlite*
%{_appdir}/include/db/*sqlite*

%files event_bbcode
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_bbcode

%files event_browsercompatibility
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_browsercompatibility

%files event_contentrewrite
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_contentrewrite

%files event_creativecommons
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_creativecommons

%files event_emoticate
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_emoticate

%files event_entryproperties
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_entryproperties

%files event_karma
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_karma

%files event_livesearch
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_livesearch

%files event_mailer
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_mailer

%files event_nl2br
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_nl2br

%files event_s9ymarkup
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_s9ymarkup

%files event_searchhighlight
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_searchhighlight

%files event_spamblock
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_spamblock

%files event_spartacus
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_spartacus

%files event_statistics
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_statistics

%files event_templatechooser
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_templatechooser

%files event_textile
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_textile

%files event_textwiki
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_textwiki

%files event_trackexits
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_trackexits

%files event_weblogping
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_weblogping

%files event_xhtmlcleanup
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_event_xhtmlcleanup

%files plugin_comments
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_plugin_comments

%files plugin_creativecommons
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_plugin_creativecommons

%files plugin_entrylinks
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_plugin_entrylinks

%files plugin_eventwrapper
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_plugin_eventwrapper

%files plugin_history
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_plugin_history

%files plugin_recententries
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_plugin_recententries

%files plugin_remoterss
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_plugin_remoterss

%files plugin_shoutbox
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_plugin_shoutbox

%files plugin_templatedropdown
%defattr(644,root,root,755)
%{_appdir}/plugins/%{name}_plugin_templatedropdown
