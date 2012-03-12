%global namedreltag .20120309gitc251f89
%global namedversion %{version}%{?namedreltag}

Name:          jboss-jms-1.1-api
Version:       1.0.1
Release:       0.1%{namedreltag}%{?dist}
Summary:       JBoss JMS API 1.1 Spec
Group:         Development/Libraries
License:       CDDL or GPLv2 with exceptions
URL:           http://www.jboss.org

# git clone git://github.com/jboss/jboss-jms-api_spec.git jboss-jms-1.1-api
# cd jboss-jms-1.1-api/ && git archive --format=tar --prefix=jboss-jms-1.1-api/ c251f89a62aa7f241367f297d4c8a7c630ab92aa | xz > jboss-jms-1.1-api-1.0.1.20120309gitc251f89.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: jboss-specs-parent
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

Requires:      jboss-specs-parent
Requires:      java
Requires:      jpackage-utils

BuildArch:     noarch

%description
The Java Messaging Service 1.1 API classes

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jms-1.1-api

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-jms-api_1.1_spec-%{version}-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE README

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE README

%changelog
* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120309gitc251f89
- Packaging after license cleanup upstream

* Tue Feb 14 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging

