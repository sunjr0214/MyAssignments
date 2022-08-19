package entities;

import entities.Reexamination;
import javax.annotation.Generated;
import javax.persistence.metamodel.CollectionAttribute;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Statusofresources.class)
public class Statusofresources_ { 

    public static volatile SetAttribute<Statusofresources, Reexamination> reexaminationCollection1;
    public static volatile SingularAttribute<Statusofresources, String> meaning;
    public static volatile SingularAttribute<Statusofresources, Integer> id;
    public static volatile CollectionAttribute<Statusofresources, Reexamination> reexaminationCollection;

}