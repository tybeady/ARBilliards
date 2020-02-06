using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;
using UnityEngine.UI;
using UnityEngine.Events;
using UnityEngine.EventSystems;

public class SkillSelect : MonoBehaviour
{
    #region Definitions
    /*Skill Level Variable*/
    int skillLevel;

    /*Camera & Cursor Components*/
    Vector3 cameraPos;

    /*Dimensions and Location of Buttons*/
    //static float x, y;
    static float x = (Screen.width) / 2;
    static float y = (Screen.height) / 2;

    static int btnWidth = 150;
    static int btnHeight = 100;

    /*Data Streaming*/
    GameObject skill_select;

    /*Objects and Sounds */
    AudioSource beep;
    GameObject canvas;
    #endregion

    #region Start and Update
    private void Start()
    {
        Cursor.visible = true;

        skill_select = GameObject.FindGameObjectWithTag("SkillLevelSelect");

        /*Generate UI*/
        BuildAudio("Audio/select_beep");
        BuildCanvas();
        BuildButton("Beginner", x - 160, y, BeginnerLevel);
        BuildButton("Moderate", x, y, ModerateLevel);
        BuildButton("Expert", x + 160, y, ExpertLevel);
    }

    private void Update()
    {
        controllerTest();
        //cameraPos = Camera.main.transform.position;
        //x = cameraPos.x;
        //y = cameraPos.y; 
    }
    /*Note:
     * We want to update our camera position constantly and assign the 
     * (x, y) location of our buttons to follow the positon of the camera.
     */
    #endregion

    #region Creating UI
    private void BuildAudio(string audioName)
    {
        beep = gameObject.AddComponent<AudioSource>();
        beep.clip = Resources.Load<AudioClip>(audioName);
        beep.playOnAwake = false;
    }
    private void BuildCanvas()
    {
        canvas = new GameObject();
        Canvas c = canvas.AddComponent<Canvas>();
        c.renderMode = RenderMode.ScreenSpaceOverlay;
        canvas.AddComponent<CanvasScaler>();
        canvas.AddComponent<GraphicRaycaster>();

        Text t = canvas.AddComponent<Text>();
        t.text = "Please Select Your Skill Level";
        t.alignment = TextAnchor.MiddleCenter;
        t.font = Resources.Load<Font>("Fonts/selawk");
        t.color = Color.black;
        t.fontSize = 30;
        t.rectTransform.position = new Vector2(x, y+85);
    }
    private void BuildButton(string btnName, float xLoc, float yLoc, UnityAction onClickAction)
    {
        if (FindObjectOfType<EventSystem>() == null)
        {
            var eventSystem = new GameObject("EventSystem", typeof(EventSystem), typeof(StandaloneInputModule));
        }

        GameObject button = new GameObject();
        button.transform.SetParent(canvas.transform, false);

        GameObject buttonText = new GameObject();
        buttonText.transform.SetParent(canvas.transform, false);

        Image i = button.AddComponent<Image>();
        i.color = Color.white;
        i.rectTransform.sizeDelta = new Vector2(btnWidth, btnHeight);
        i.rectTransform.position = new Vector2(xLoc, yLoc);

        Text t = buttonText.AddComponent<Text>();
        t.transform.SetParent(i.transform, false);
        t.text = btnName;
        t.alignment = TextAnchor.MiddleCenter;
        t.font = Resources.Load<Font>("Fonts/selawk");
        t.color = Color.black;
        t.fontSize = 20;
        t.rectTransform.sizeDelta = new Vector2(btnWidth, btnHeight);
        t.rectTransform.position = new Vector2(xLoc, yLoc);

        Button b = button.AddComponent<Button>();
        b.onClick.AddListener(beep.Play);
        b.onClick.AddListener(onClickAction);
    }
    /*Note:
     * Here we generate a blank canvas and attach our button(s).
     * We define our button shape, size, color, and text.
     * We also specify what action is completed on button press. 
     */
    #endregion

    #region Define Actions for Button Click
    public void BeginnerLevel()
    {
        skillLevel = 0; //Debug.Log(skillLevel);
        skill_select.GetComponent<ClientApplication>().Post("SkillLevel", skillLevel.ToString());
        StartCoroutine(ChangeScene(0.5f));
    }
    public void ModerateLevel()
    {
        skillLevel = 1; //Debug.Log(skillLevel);
        skill_select.GetComponent<ClientApplication>().Post("SkillLevel", skillLevel.ToString());
        StartCoroutine(ChangeScene(0.5f));
    }
    public void ExpertLevel()
    {
        skillLevel = 2; //Debug.Log(skill_level);
        skill_select.GetComponent<ClientApplication>().Post("SkillLevel", skillLevel.ToString());
        StartCoroutine(ChangeScene(0.5f));
    }
    IEnumerator ChangeScene(float time)
    {
        yield return new WaitForSeconds(time);
        SceneManager.LoadScene(sceneName: "Main");
    }
    /*Note:
     * Here we have defined our three skill levels and the actions 
     * that occur when these functions are called.
     */
    #endregion

    #region Controller Testing?
    void controllerTest()
    {
        if (Input.GetKeyDown(KeyCode.JoystickButton0))
        {
            Debug.Log("Button A was pressed.");
        }

        if (Input.GetKeyDown(KeyCode.JoystickButton1))
        {
            Debug.Log("Button B was pressed.");
        }

        if (Input.GetKeyDown(KeyCode.JoystickButton3))
        {
            Debug.Log("Button Y was pressed.");
        }

        if (Input.GetKeyDown(KeyCode.JoystickButton2))
        {
            Debug.Log("Button X was pressed.");
        }

        if (Mathf.Abs(Input.GetAxis("JoyLeftX")) > 0.2 || Mathf.Abs(Input.GetAxis("JoyLeftY")) > 0.2)
        {
            Debug.Log(Input.GetJoystickNames() + " is moved");
        }

        if (Mathf.Abs(Input.GetAxis("JoyRightX")) > 0.2 || Mathf.Abs(Input.GetAxis("JoyRightY")) > 0.2)
        {
            Debug.Log(Input.GetJoystickNames() + " is moved");
        }
    } 
    #endregion

}