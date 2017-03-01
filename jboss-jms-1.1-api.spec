%{?scl:%scl_package jboss-jms-1.1-api}
%{!?scl:%global pkg_name %{name}}

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:		%{?scl_prefix}jboss-jms-1.1-api
Version:	1.0.1
Release:	15%{?dist}
Summary:	JBoss JMS API 1.1 Spec
License:	CDDL or GPLv2 with exceptions
URL:		http://www.jboss.org

# git clone git://github.com/jboss/jboss-jms-api_spec.git jboss-jms-1.1-api
# cd jboss-jms-1.1-api/ && git archive --format=tar --prefix=jboss-jms-1.1-api/ jboss-jms-api_1.1_spec-1.0.1.Final | xz > jboss-jms-1.1-api-1.0.1.Final.tar.xz
Source0:	%{pkg_name}-%{namedversion}.tar.xz

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_maven}maven-plugin-bundle
BuildRequires:	%{?scl_prefix_maven}jboss-parent
%{?scl:Requires: %scl_runtime}
BuildArch:	noarch

%description
The Java Messaging Service 1.1 API classes

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{pkg_name}
# Unneeded plugin
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%pom_remove_plugin :maven-source-plugin
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README
%license LICENSE

%changelog
* Wed Mar 01 2017 Tomas Repik <trepik@redhat.com> - 1.0.1-15
- scl conversion

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.0.1-13
- Add missing BuildRequires to fix FTBFS (BZ#1405232).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 gil cattaneo <puntogil@libero.it> 1.0.1-11
- fix FTBFS rhbz#1239594
- fix BR list and use BRs mvn()-like
- minor changes for adapt to current guideline
- introduce license macro
- resolve some rpmlint problem

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 01 2014 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-9
- New guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.1-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-3
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release 1.0.1.Final
- Fixed R and BR

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120309gitc251f89
- Packaging after license cleanup upstream

* Mon Feb 14 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging

