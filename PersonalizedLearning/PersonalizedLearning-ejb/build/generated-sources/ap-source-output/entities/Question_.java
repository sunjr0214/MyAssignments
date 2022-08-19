package entities;

import entities.Knowledge;
import entities.Praise;
import entities.Questionstudentcosttime;
import entities.Reexamination;
import entities.WrongquestionCollection;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Question.class)
public class Question_ { 

    public static volatile SingularAttribute<Question, String> figure;
    public static volatile SingularAttribute<Question, Integer> needtime;
    public static volatile SetAttribute<Question, Praise> praiseSet;
    public static volatile SetAttribute<Question, WrongquestionCollection> wrongquestionCollectionSet;
    public static volatile SingularAttribute<Question, Integer> degree;
    public static volatile SingularAttribute<Question, String> secondcontent;
    public static volatile SingularAttribute<Question, Integer> type;
    public static volatile SingularAttribute<Question, String> analysis;
    public static volatile SetAttribute<Question, Reexamination> reexaminationSet;
    public static volatile SingularAttribute<Question, Integer> praiseCnt;
    public static volatile SingularAttribute<Question, Knowledge> knowledgeId;
    public static volatile SingularAttribute<Question, Integer> score;
    public static volatile SingularAttribute<Question, String> answer;
    public static volatile SingularAttribute<Question, String> refer;
    public static volatile SingularAttribute<Question, String> valueinfo;
    public static volatile SingularAttribute<Question, Integer> id;
    public static volatile SetAttribute<Question, Questionstudentcosttime> questionstudentcosttimeSet;

}