using UnityEngine;
public class SkillSelect : MonoBehaviour
{
    #region Definitions
    /* Skill Level Variable */
    int skillLevel;

    /* Dimensions */
    //static float x, y;
    static float x = (Screen.width) / 2;
    static float y = (Screen.height) / 2;

    /* Camera & Cursor Components */
    Vector3 cameraPos;

    /* Game Objects */
    GameObject skill_select;
    #endregion

    #region Start and Update
    private void Start()
    {
        skill_select = GameObject.FindGameObjectWithTag("SkillLevelSelect");

        /* Generate UI */
        skill_select.GetComponent<BuildUI>().BuildAudio("Audio/scene_sound", "Audio/select_sound");
        skill_select.GetComponent<BuildUI>().BuildCanvas();
        skill_select.GetComponent<BuildUI>().UpdateCanvasText("Please Select Your Skill Level");
        skill_select.GetComponent<BuildUI>().BuildButton("Beginner", x - 160, y, BeginnerLevel);
        skill_select.GetComponent<BuildUI>().BuildButton("Moderate", x, y, ModerateLevel);
        skill_select.GetComponent<BuildUI>().BuildButton("Expert", x + 160, y, ExpertLevel);
    }

    private void Update()
    {
        //controllerTest();
        //cameraPos = Camera.main.transform.position;
        //x = cameraPos.x;
        //y = cameraPos.y; 
    }
    /*Note:
     * We want to update our camera position constantly and assign the 
     * (x, y) location of our buttons to follow the positon of the camera.
     */
    #endregion

    #region Actions on Button Click
    public void BeginnerLevel()
    {
        skillLevel = 0; //Debug.Log(skillLevel);
        skill_select.GetComponent<ClientApplication>().Post("UserSkillLevel", skillLevel.ToString());
        skill_select.GetComponent<BuildUI>().PlaySceneSound().Invoke();
        StartCoroutine(skill_select.GetComponent<Actions>().ChangeScene(0.5f, "Table Position Calibration"));
    }
    public void ModerateLevel()
    {
        skillLevel = 1; //Debug.Log(skillLevel);
        skill_select.GetComponent<ClientApplication>().Post("UserSkillLevel", skillLevel.ToString());
        skill_select.GetComponent<BuildUI>().PlaySceneSound().Invoke();
        StartCoroutine(skill_select.GetComponent<Actions>().ChangeScene(0.5f, "Table Position Calibration"));
    }
    public void ExpertLevel()
    {
        skillLevel = 2; //Debug.Log(skill_level);
        skill_select.GetComponent<ClientApplication>().Post("UserSkillLevel", skillLevel.ToString());
        skill_select.GetComponent<BuildUI>().PlaySceneSound().Invoke();
        StartCoroutine(skill_select.GetComponent<Actions>().ChangeScene(0.5f, "Table Position Calibration"));
    }
    #endregion

}