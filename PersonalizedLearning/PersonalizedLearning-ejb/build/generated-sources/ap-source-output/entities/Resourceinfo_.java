package entities;

import entities.Resourceinfo;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:13")
@StaticMetamodel(Resourceinfo.class)
public class Resourceinfo_ { 

    public static volatile SingularAttribute<Resourceinfo, Integer> menuorder;
    public static volatile SetAttribute<Resourceinfo, Resourceinfo> resourceinfoSet;
    public static volatile SingularAttribute<Resourceinfo, String> name;
    public static volatile SingularAttribute<Resourceinfo, String> valueinfo;
    public static volatile SingularAttribute<Resourceinfo, Integer> id;
    public static volatile SingularAttribute<Resourceinfo, Resourceinfo> parentid;

}