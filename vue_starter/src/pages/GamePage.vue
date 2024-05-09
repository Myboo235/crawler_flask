<template>
    <div class="p-[2rem] bg-secondary fixed top-0 left-0 h-full">
        <h2 class="mb-[1rem] text-2xl"><b>Topics</b></h2>
        <ul>
            <li class="px-[1rem] py-[1rem] rounded-lg hover:underline cursor-pointer" v-for="topic in topics"
                :key="topic" @click="changeTopic(topic)">{{ topic }}</li>
        </ul>
    </div>
    <div class="flex justify-center">
        <div class="ml-[10rem] p-[2rem]">
            <div class="text-black" v-if="filteredData.length">
                <template v-for="(topic, index) in topics" :key="index">
                    <div v-if="filteredData.filter(item => item.topic === topic).length > 0" :id="`topic-${topic}`"
                        class="bg-secondary rounded-xl p-[0.5rem] my-[2rem]" :key="topic">
                        <h3 class="mb-[1rem] text-lg font-bold">
                            {{ topic }}
                        </h3>
                        <template v-for="item in filteredData" :key="item.id">
                            <div v-if="item.topic === topic" class="bg-white cursor-pointer p-[1rem] rounded-xl my-4"
                                @click="toggleAnswer(item)">
                                <div class="font-bold">{{ item.ques }}</div>
                                <div :class="{ 'blur-text': !item.showAnswer && isBlurred }" class="answer">
                                    {{ item.ans }}
                                </div>
                            </div>
                        </template>
                        <button
                            class="p-[0.5rem] hover:bg-primary hover:text-secondary hover:underline cursor-pointer rounded-xl"
                            @click="toggleAnswersForBorder(topic)">
                            {{ isBorderVisible(topic) ? 'Hide answers' : 'Show answers' }}
                        </button>
                    </div>
                </template>
            </div>
            <div v-else class="no-data">No data available.</div>
        </div>

    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const getData = async () => {
    const api_url = "http://localhost:5173/api.json";
    const response = await fetch(api_url);
    const data = await response.json();
    data.forEach(item => item.showAnswer = false);
    return data;
}

const data = ref(null);
const filteredData = ref([]);
const currentTopic = ref(null);
const allAnswersVisible = ref(false);
const isBlurred = ref(true); // Biến kiểm soát độ mờ 
const topics = ref([]);

const changeTopic = (topic) => {
    currentTopic.value = topic;
    const element = document.getElementById(`topic-${topic}`);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
};

const filterData = () => {
    if (!data.value) {
        filteredData.value = [];
        return;
    }
    if (!currentTopic.value) {
        filteredData.value = data.value;
    } else {
        filteredData.value = data.value.filter(item => item.topic === currentTopic.value);
    }
};

const toggleAllAnswers = () => {
    allAnswersVisible.value = !allAnswersVisible.value;
    isBlurred.value = !allAnswersVisible.value; // Toggle isBlurred dựa trên allAnswersVisible
};

const toggleAnswersForBorder = (topic) => {
    filteredData.value.forEach(item => {
        if (item.topic === topic) {
            item.showAnswer = !item.showAnswer;
        }
    });
    isBlurred.value = true; // Làm mờ khi ẩn câu trả lời
};

const isBorderVisible = (topic) => {
    return filteredData.value.some(item => item.topic === topic && item.showAnswer);
};

const toggleAnswer = (item) => {
    item.showAnswer = !item.showAnswer;
    isBlurred.value = true; // Làm mờ khi hiding an answer
};

const extractTopics = () => {
    if (!data.value) return;
    const uniqueTopics = [...new Set(data.value.map(item => item.topic))];
    topics.value = uniqueTopics;
};

onMounted(() => {
    getData().then(result => {
        data.value = result;
        filterData();
        extractTopics();
    });
});
</script>

<style scoped>
.blur-text {
    filter: blur(4px);
}
</style>
