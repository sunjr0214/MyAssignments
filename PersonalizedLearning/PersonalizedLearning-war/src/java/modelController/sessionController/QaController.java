package modelController.sessionController;

import java.io.Serializable;
import javax.enterprise.context.SessionScoped;
import javax.inject.Named;

@Named
@SessionScoped
public class QaController implements Serializable {

    private String question;
    private String answer;
    
    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }

    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }
    
    public void submit() {
        this.answer = "不知道怎么回答：" + this.question;
    }

}
