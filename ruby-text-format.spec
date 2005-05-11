%define		ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define		ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')

Summary:	A Ruby port of Text::Format
Summary(pl):	Port Text::Format dla jêzyka Ruby
Name:		ruby-Text-Format
Version:	0.64
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.halostatue.ca/files/text-format-%{version}.tar.gz
# Source0-md5:	f9e1aa720f39fffd4c83aeae4ba9e90f
Source1:	setup.rb
URL:		http://www.halostatue.ca/ruby/Text__Format.html	
BuildRequires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Format provides strong text formatting capabilities to Ruby.
Based on Perl's Text::Format 0.52, it offers all of the functionality
of that module and new capabilities besides. 

%description -l pl
Text::Format udostêpnia potê¿ne mo¿liwo¶ci formatowania tekstu w
jêzyku Ruby. Jest oparty na perlowym Text::Format 0.52 i oferuje ca³±
funkcjonalno¶æ tego modu³u, a przy okazji nowe funkcje.

%prep
%setup -n text-format-%{version}

%build
cp %{SOURCE1} .
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir}

ruby setup.rb setup
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
